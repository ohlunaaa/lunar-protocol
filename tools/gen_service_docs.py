#!/usr/bin/env python3
"""
Generate per-service markdown documentation from the extracted
protobuf files in proto/extracted/.

Parses the re-emitted .proto text files and produces one markdown file
per service (plus a shared-types doc), covering:
  - the service definition with all RPCs
  - every message with its fields, recursively
  - enums with values
  - imports (dependencies)

Output: docs/services/<n>.md
"""
import os
import re
import sys
import collections

SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join("proto", "extracted")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join("docs", "services")

PKG_RE = re.compile(r'^package\s+([\w.]+)\s*;')
IMPORT_RE = re.compile(r'^import\s+"([^"]+)"\s*;')
SERVICE_RE = re.compile(r'^service\s+(\w+)\s*\{')
RPC_RE = re.compile(r'rpc\s+(\w+)\s*\(\s*([\w.]+)\s*\)\s*returns\s*\(\s*([\w.]+)\s*\)')
ENUM_RE = re.compile(r'^enum\s+(\w+)\s*\{')
ENUM_VAL_RE = re.compile(r'^\s*(\w+)\s*=\s*(-?\w+)\s*;')
MSG_RE = re.compile(r'^message\s+(\w+)\s*\{')
ONEOF_RE = re.compile(r'^\s*oneof\s+(\w+)\s*\{')
FIELD_RE = re.compile(
    r'^\s*(?:(repeated|optional|required)\s+)?'
    r'([\w.]+(?:\.[A-Z]\w+)*)\s+'
    r'(\w+)\s*=\s*(\d+)\s*(?:\[(.*?)\])?\s*;')


class Enum:
    def __init__(self, name):
        self.name = name
        self.values = []  # (name, number)


class Field:
    def __init__(self, label, type_, name, number, oneof=None):
        self.label = label or ""
        self.type = type_
        self.name = name
        self.number = int(number)
        self.oneof = oneof


class Message:
    def __init__(self, name):
        self.name = name
        self.fields = []
        self.oneofs = []          # oneof names in order
        self.enums = []           # nested enums
        self.messages = []        # nested messages


class Service:
    def __init__(self, name):
        self.name = name
        self.rpcs = []            # (method, input, output)


def strip_comments(text):
    text = re.sub(r'//[^\n]*', '', text)
    return text


def parse_proto(text):
    pkg = ""
    imports = []
    enums, messages, services = [], [], []
    # stack-based parse
    msg_stack = []
    enum_stack = []
    oneof_stack = []
    cur_oneof = None
    for line in strip_comments(text).splitlines():
        line_s = line.strip()
        m = PKG_RE.match(line_s)
        if m and not pkg:
            pkg = m.group(1)
            continue
        m = IMPORT_RE.match(line_s)
        if m:
            imports.append(m.group(1))
            continue
        # close scopes
        if line_s == "}":
            if enum_stack:
                enum_stack.pop()
                continue
            if oneof_stack:
                oneof_stack.pop()
                continue
            if msg_stack:
                msg_stack.pop()
                continue
            continue
        m = ENUM_RE.match(line_s)
        if m:
            e = Enum(m.group(1))
            target = msg_stack[-1] if msg_stack else None
            if target:
                target.enums.append(e)
            else:
                enums.append(e)
            enum_stack.append(e)
            continue
        if enum_stack:
            m = ENUM_VAL_RE.match(line)
            if m:
                enum_stack[-1].values.append((m.group(1), m.group(2)))
            continue
        m = ONEOF_RE.match(line)
        if m:
            oneof_stack.append(m.group(1))
            if msg_stack:
                msg_stack[-1].oneofs.append(m.group(1))
            cur_oneof = m.group(1)
            continue
        if oneof_stack:
            cur_oneof = oneof_stack[-1]
        else:
            cur_oneof = None
        m = MSG_RE.match(line_s)
        if m:
            msg = Message(m.group(1))
            if msg_stack:
                msg_stack[-1].messages.append(msg)
            else:
                messages.append(msg)
            msg_stack.append(msg)
            continue
        if msg_stack:
            fm = FIELD_RE.match(line)
            if fm and not line_s.startswith(("rpc", "service", "enum",
                                             "message", "oneof")):
                msg_stack[-1].fields.append(Field(
                    fm.group(1), fm.group(2), fm.group(3),
                    fm.group(4), cur_oneof))
            continue
        m = SERVICE_RE.match(line_s)
        if m:
            services.append(Service(m.group(1)))
            continue
        if services:
            rm = RPC_RE.match(line_s)
            if rm:
                services[-1].rpcs.append(
                    (rm.group(1), rm.group(2), rm.group(3)))
    return pkg, imports, enums, messages, services


SCALAR_TYPES = {"double", "float", "int32", "int64", "uint32", "uint64",
                "sint32", "sint64", "fixed32", "fixed64", "sfixed32",
                "sfixed64", "bool", "string", "bytes"}


def fmt_enum(e, indent=""):
    lines = [f"{indent}- enum **{e.name}**:"]
    for n, v in e.values:
        lines.append(f"{indent}  - `{n} = {v}`")
    return lines


def fmt_message(msg, all_msgs, indent=0, seen=None):
    """Render a message section; resolve nested recursively."""
    if seen is None:
        seen = set()
    pad = "  " * indent
    key = msg.name
    if key in seen:
        return [f"{pad}- **{msg.name}** _(recursion omitted)_"]
    seen = set(seen)
    seen.add(key)
    lines = [f"{pad}- **{msg.name}**"]
    if msg.oneofs:
        for o in msg.oneofs:
            lines.append(f"{pad}  - oneof `{o}`:")
    for f in msg.fields:
        t = f.type
        tdisp = f"`{t}`" if t in SCALAR_TYPES else f"`{t}`"
        lbl = f"{f.label} " if f.label else ""
        oneof = f" _({f.oneof})_" if f.oneof else ""
        lines.append(
            f"{pad}  - {lbl}{tdisp} `{f.name}` = {f.number}{oneof}")
    for e in msg.enums:
        lines.extend(fmt_enum(e, pad + "  "))
    for nested in msg.messages:
        lines.extend(fmt_message(nested, all_msgs, indent + 1, seen))
    return lines


def main():
    os.makedirs(OUT, exist_ok=True)
    files = sorted(f for f in os.listdir(SRC) if f.endswith(".proto"))
    service_docs = {}
    shared_msgs = []
    shared_enums = []

    for fname in files:
        path = os.path.join(SRC, fname)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        pkg, imports, enums, messages, services = parse_proto(text)
        rel = fname.replace("_", "/").replace("/v/1", "/v1")
        rel = fname  # keep filename as-is for links

        # group: attach common/push messages to their service doc
        base = fname.replace("lunarclient_", "").replace(".proto", "")
        parts = base.split("_")
        # find "v1"/"v2" to split pkg vs kind
        kind = parts[-1]  # common / push / service / schema / button/...
        svc_key = "_".join(parts[:-1]) if len(parts) > 1 else base

        if services:
            for svc in services:
                key = svc_key
                doc = service_docs.setdefault(
                    key, {"package": pkg, "services": [],
                          "messages": [], "enums": [], "imports": []})
                doc["services"].append((svc, fname))
                doc["imports"] = list(
                    set(doc["imports"]) | set(imports))
                doc["messages"].extend(messages)
                doc["enums"].extend(enums)
        else:
            # shared types doc
            shared_msgs.append((pkg, messages, fname))
            shared_enums.append((pkg, enums, fname))

    # write service docs
    index = ["# Services", "",
             "Auto-generated from `proto/extracted/`.", ""]
    for key in sorted(service_docs):
        doc = service_docs[key]
        title = key.replace("_", ".")
        lines = [f"# `{doc['package']}`", ""]
        for svc, fname in doc["services"]:
            lines.append(f"## Service `{svc.name}`")
            lines.append("")
            lines.append(f"Source: [`proto/extracted/{fname}`]"
                         f"(../../proto/extracted/{fname})")
            lines.append("")
            lines.append("| Method | Request | Response |")
            lines.append("|---|---|---|")
            for m, i, o in svc.rpcs:
                lines.append(f"| `{m}` | `{i}` | `{o}` |")
            lines.append("")
        if doc["enums"]:
            lines.append("## Enums")
            lines.append("")
            for e in doc["enums"]:
                lines.extend(fmt_enum(e))
            lines.append("")
        if doc["messages"]:
            lines.append("## Messages")
            lines.append("")
            for m in doc["messages"]:
                lines.extend(fmt_message(m, doc["messages"]))
            lines.append("")
        outp = os.path.join(OUT, f"{key}.md")
        with open(outp, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))
        index.append(f"- [`{doc['package']}`]({key}.md)"
                     f" ({sum(len(s.rpcs) for s, _ in doc['services'])} RPCs)")

    # shared types doc
    lines = ["# Shared Types", "",
             "Messages and enums without a service "
             "(common/push schemas).", ""]
    for pkg, msgs, fname in shared_msgs:
        if not msgs:
            continue
        lines.append(f"## `{pkg}` "
                     f"([source](../../proto/extracted/{fname}))")
        lines.append("")
        for m in msgs:
            lines.extend(fmt_message(m, msgs))
        lines.append("")
    for pkg, enums, fname in shared_enums:
        if not enums:
            continue
        lines.append(f"## `{pkg}` enums "
                     f"([source](../../proto/extracted/{fname}))")
        lines.append("")
        for e in enums:
            lines.extend(fmt_enum(e))
        lines.append("")
    with open(os.path.join(OUT, "_shared.md"), "w",
              encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    index.append("- [Shared types](_shared.md)")

    with open(os.path.join(OUT, "index.md"), "w",
              encoding="utf-8") as fh:
        fh.write("\n".join(index) + "\n")
    print(f"generated {len(service_docs)} service docs + shared -> {OUT}")


if __name__ == "__main__":
    main()
