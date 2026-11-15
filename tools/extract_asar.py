"""
Minimal ASAR archive extractor (Electron archive format).

Format:
  UInt32 (LE): header pickle size field (usually 4)
  UInt32 (LE): JSON header string size
  JSON header (that many bytes) - file tree with offsets relative
               to the end of the aligned header block
  padding to 4-byte alignment
  file data blob

Usage: python extract_asar.py <app.asar> <outdir>
"""
import json
import os
import struct
import sys


def read_header(data):
    # Chromium pickle layout for ASAR:
    #   UInt32 LE [0:4]  = pickle payload size (usually 4)
    #   UInt32 LE [4:8]  = total header size (pickle-wrapped)
    #   UInt32 LE [8:12] = header size (string length field)
    #   UInt32 LE [12:16]= JSON string length
    #   JSON starts at byte 16
    json_size = struct.unpack("<I", data[12:16])[0]
    header_json = data[16:16 + json_size].decode("utf-8")
    header = json.loads(header_json)
    # Data starts after the aligned header block.
    base = (16 + json_size + 3) & ~3  # align to 4
    return header, base


def walk(node, prefix, header_base, data, outdir):
    for name, entry in node.get("files", {}).items():
        path = os.path.join(prefix, name) if prefix else name
        if "files" in entry:
            # directory
            os.makedirs(os.path.join(outdir, path), exist_ok=True)
            walk(entry, path, header_base, data, outdir)
        else:
            if "offset" not in entry:
                continue  # unpacked/external entry (lives in app.asar.unpacked)
            size = entry["size"]
            offset = int(entry["offset"])
            start = header_base + offset
            out = os.path.join(outdir, path)
            os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
            with open(out, "wb") as f:
                f.write(data[start:start + size])


def main():
    asar_path, outdir = sys.argv[1], sys.argv[2]
    with open(asar_path, "rb") as f:
        data = f.read()
    header, base = read_header(data)
    os.makedirs(outdir, exist_ok=True)
    walk(header, "", base, data, outdir)
    # also dump the raw header JSON for inspection
    with open(os.path.join(outdir, "_header.json"), "w", encoding="utf-8") as f:
        json.dump(header, f, indent=2)
    count = sum(len(fs) for _, _, fs in os.walk(outdir))
    print(f"extracted {count} files -> {outdir}")


if __name__ == "__main__":
    main()
