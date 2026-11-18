#!/usr/bin/env python3
"""news-image-20261117 entry: copy the bundled front-page image to the
output directory.

The image (entry.png, a 1024x1024 PNG) is a newspaper front page,
"THE WORLD IN ONE PAGE", summing up Tuesday 17 November 2026: the
Kerch Bridge collapse and the Kyiv bridge strikes, the Iran/Gulf
drone and tanker incidents, Trump's Asia trip and the Xi-Trump-Putin
meeting, Nvidia's first post-Huang earnings and the US chip curbs,
the JPMorgan outage, the Pentagon's ninth failed audit, and an
"Also today" strip. It was rendered once with PIL from headlines
researched on 18 November 2026 and is shipped in this repository.
This program only copies it verbatim: no network, no randomness, no
timestamps, so repeated runs produce identical bytes.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Fail loudly instead of shipping a truncated copy, and prove the
    # copy is a whole PNG identical to the bundled image.
    with open(dst, "rb") as fh:
        data = fh.read()
    if data[:8] != PNG_MAGIC:
        raise RuntimeError("entry.png copy is not a PNG")
    if len(data) != os.path.getsize(src):
        raise RuntimeError("entry.png copy is incomplete")
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {dst} ({len(data)} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
