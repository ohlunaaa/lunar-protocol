"""
Extract embedded protobuf FileDescriptorProto blobs from generated
*Proto.class files inside the extracted lunar.jar.

Java .class constant pool: tag 1 = Utf8 (u2 length + bytes).
The generated classes hold the serialized descriptor as a raw
modified-UTF-8 string (protobuf-java 3.x style, not Base64).

Decodes each blob with a minimal protobuf wire parser and emits
readable .proto text.
"""
import base64
import os
import struct
import sys

JAR_DIR = sys.argv[1] if len(sys.argv) > 1 else "jar"
OUT_DIR = sys.argv[2] if len(sys.argv) > 2 else "protos"


def read_utf8_strings(path):
    """Parse .class constant pool, return all Utf8 strings.

    Java class files use modified UTF-8: NUL is 0xC0 0x80 and codepoints
    are standard otherwise. Descriptor blobs are ISO-8859-1 bytes, so we
    decode codepoints and map each back to one byte.
    """
    with open(path, "rb") as f:
        data = f.read()
    if data[:4] != b"\xca\xfe\xba\xbe":
        return []
    minor, major, count = struct.unpack(">HHH", data[4:10])
    i = 0
    strings = []
    pos = 10
    while i < count - 1:
        i += 1
        tag = data[pos]
        pos += 1
        if tag == 1:  # Utf8
            ln = struct.unpack(">H", data[pos:pos + 2])[0]
            pos += 2
            raw = data[pos:pos + ln]
            pos += ln
            strings.append(decode_modified_utf8(raw))
        elif tag in (7, 8, 16, 19, 20):  # single u2 index
            pos += 2
        elif tag == 15:  # MethodHandle
            pos += 3
        elif tag in (3, 4, 9, 10, 11, 12, 17, 18):  # u4 or 2x u2
            pos += 4
        elif tag in (5, 6):  # long/double: 8 bytes, takes 2 slots
            pos += 8
            i += 1
        else:
            break  # unknown tag -> bail
    return strings


def decode_modified_utf8(raw: bytes) -> bytes:
    """Decode Java modified UTF-8 back to the original ISO-8859-1 bytes."""
    out = bytearray()
    i = 0
    n = len(raw)
    while i < n:
        b = raw[i]
        if b == 0 or b >= 0xF0:
            i += 1  # invalid, skip
        elif b < 0x80:
            out.append(b)
            i += 1
        elif b == 0xC0 and i + 1 < n and raw[i + 1] == 0x80:
            out.append(0)
            i += 2
        elif 0xC2 <= b <= 0xDF and i + 1 < n:
            out.append(((b & 0x1F) << 6) | (raw[i + 1] & 0x3F))
            i += 2
        elif 0xE0 <= b <= 0xEF and i + 2 < n:
            cp = ((b & 0x0F) << 12) | ((raw[i + 1] & 0x3F) << 6) | (raw[i + 2] & 0x3F)
            # surrogate pair handling for supplementary chars
            if 0xD800 <= cp <= 0xDBFF and i + 5 < n and raw[i + 3] == 0xED:
                lo = ((raw[i + 4] & 0x3F) << 6) | (raw[i + 5] & 0x3F)
                full = 0x10000 + ((cp - 0xD800) << 10) + (lo - 0xDC00)
                out.extend(full.to_bytes(4, "big"))  # rare in descriptors
                i += 6
            else:
                out.append(cp & 0xFF)  # BMP > 0xFF shouldn't occur in ISO-8859-1 blobs
                out.append((cp >> 8) & 0xFF) if cp > 0xFF else None
                i += 3
        else:
            i += 1
    return bytes(out)


def is_base64(s: bytes) -> bool:
    if len(s) < 50:
        return False
    try:
        base64.b64decode(s, validate=True)
        return True
    except Exception:
        return False


# --- minimal protobuf wire reader ---

def read_varint(buf, pos):
    result = 0
    shift = 0
    while True:
        b = buf[pos]
        pos += 1
        result |= (b & 0x7F) << shift
        if not b & 0x80:
            return result, pos
        shift += 7


def parse_fields(buf):
    """Yield (field_number, wire_type, value) tuples."""
    pos = 0
    while pos < len(buf):
        key, pos = read_varint(buf, pos)
        fn, wt = key >> 3, key & 7
        if wt == 0:
            v, pos = read_varint(buf, pos)
            yield fn, wt, v
        elif wt == 2:
            ln, pos = read_varint(buf, pos)
            yield fn, wt, buf[pos:pos + ln]
            pos += ln
        elif wt == 5:
            yield fn, wt, struct.unpack("<I", buf[pos:pos + 4])[0]
            pos += 4
        elif wt == 1:
            yield fn, wt, struct.unpack("<Q", buf[pos:pos + 8])[0]
            pos += 8
        else:
            raise ValueError(f"wire type {wt}")


def as_msg(b):
    return list(parse_fields(b))


def as_str(b):
    return b.decode("utf-8", "replace")


# --- FileDescriptorProto model ---

TYPES = {1: "double", 2: "float", 3: "int64", 4: "uint64", 5: "int32",
         6: "fixed64", 7: "fixed32", 8: "bool", 9: "string", 12: "bytes",
         13: "uint32", 15: "sfixed32", 16: "sfixed64", 17: "sint32",
         18: "sint64"}
LABELS = {1: "optional", 2: "required", 3: "repeated"}


def parse_field(b):
    f = {"name": "", "number": 0, "label": 1, "type": 0, "type_name": "",
         "oneof": None}
    for fn, wt, v in parse_fields(b):
        if fn == 1: f["name"] = as_str(v)
        elif fn == 3: f["number"] = v
        elif fn == 4: f["label"] = v
        elif fn == 5: f["type"] = v
        elif fn == 6: f["type_name"] = as_str(v)
        elif fn == 8: f["oneof"] = v
    return f


def parse_enum(b):
    name, values = "", []
    for fn, wt, v in parse_fields(b):
        if fn == 1: name = as_str(v)
        elif fn == 2:
            vn, vnum = "", 0
            for f2, w2, v2 in parse_fields(v):
                if f2 == 1: vn = as_str(v2)
                elif f2 == 2: vnum = v2
            values.append((vn, vnum))
    return name, values


def parse_message(b, indent=1):
    out = []
    name = ""
    fields, nested, enums, oneofs = [], [], [], []
    for fn, wt, v in parse_fields(b):
        if fn == 1: name = as_str(v)
        elif fn == 2: fields.append(parse_field(v))
        elif fn == 3: nested.append(v)
        elif fn == 4: enums.append(v)
        elif fn == 8: oneofs.append(as_str(v))
    pad = "  " * indent
    out.append(f"{pad[:-2]}message {name} {{")
    for on in oneofs:
        out.append(f"{pad}oneof {on} {{")
        for f in fields:
            if f["oneof"] is not None and oneofs.index(on) == f["oneof"]:
                out.append(field_line(f, indent + 2))
        out.append(f"{pad}}}")
    for en, vals in [parse_enum(e) for e in enums]:
        out.append(f"{pad}enum {en} {{")
        for vn, vnum in vals:
            out.append(f"{pad}  {vn} = {vnum};")
        out.append(f"{pad}}}")
    for f in fields:
        if f["oneof"] is None:
            out.append(field_line(f, indent + 1))
    for n in nested:
        out.extend(parse_message(n, indent + 1))
    out.append(f"{pad[:-2]}}}")
    return out


def field_line(f, indent):
    pad = "  " * indent
    t = f["type_name"].lstrip(".") if f["type_name"] else TYPES.get(f["type"], f"type")
    lbl = "repeated " if f["label"] == 3 else ""
    return f"{pad}{lbl}{t} {f['name']} = {f['number']};"


def parse_method(b):
    name, inp, out = "", "", ""
    for fn, wt, v in parse_fields(b):
        if fn == 1: name = as_str(v)
        elif fn == 2: inp = as_str(v)
        elif fn == 3: out = as_str(v)
    return name, inp.lstrip("."), out.lstrip(".")


def parse_service(b):
    name, methods = "", []
    for fn, wt, v in parse_fields(b):
        if fn == 1: name = as_str(v)
        elif fn == 2: methods.append(parse_method(v))
    return name, methods


def parse_file(b):
    name, pkg, deps, msgs, enums, svcs = "", "", [], [], [], []
    for fn, wt, v in parse_fields(b):
        if fn == 1: name = as_str(v)
        elif fn == 2: pkg = as_str(v)
        elif fn == 3: deps.append(as_str(v))
        elif fn == 4: msgs.append(v)
        elif fn == 5: enums.append(v)
        elif fn == 6: svcs.append(v)
    return name, pkg, deps, msgs, enums, svcs


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    proto_classes = []
    for root, _, files in os.walk(os.path.join(JAR_DIR, "com", "lunarclient")):
        for f in files:
            if f.endswith("Proto.class"):
                proto_classes.append(os.path.join(root, f))
    print(f"{len(proto_classes)} *Proto.class files")

    seen, written = set(), 0
    for pc in sorted(proto_classes):
        for s in read_utf8_strings(pc):
            # raw FileDescriptorProto: starts with field 1 (name), wire 2
            if len(s) > 30 and s[:1] == b"\n" and b".proto" in s[:80]:
                try:
                    blob = s
                    name, pkg, deps, msgs, enums, svcs = parse_file(blob)
                    if not name.endswith(".proto") or name in seen:
                        continue
                    seen.add(name)
                except Exception:
                    continue
                lines = ['syntax = "proto3";', f"package {pkg};", ""]
                for d in deps:
                    lines.append(f'import "{d}";')
                if deps: lines.append("")
                for en, vals in [parse_enum(e) for e in enums]:
                    lines.append(f"enum {en} {{")
                    for vn, vnum in vals:
                        lines.append(f"  {vn} = {vnum};")
                    lines.append("}")
                for m in msgs:
                    lines.extend(parse_message(m))
                    lines.append("")
                for sn, methods in [parse_service(s) for s in svcs]:
                    lines.append(f"service {sn} {{")
                    for mn, mi, mo in methods:
                        lines.append(f"  rpc {mn}({mi}) returns ({mo});")
                    lines.append("}")
                out = os.path.join(OUT_DIR, name.replace("/", "_"))
                with open(out, "w", encoding="utf-8") as fh:
                    fh.write("\n".join(lines) + "\n")
                written += 1
                print(f"  + {name} ({len(msgs)} msgs, {len(svcs)} services)")
    print(f"\n{written} .proto files -> {OUT_DIR}")


if __name__ == "__main__":
    main()
