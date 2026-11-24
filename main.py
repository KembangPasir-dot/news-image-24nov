#!/usr/bin/env python3
"""Copy the bundled entry image to the output directory.

make.fun entrypoint (Python 3.13, standard library only): the program
runs twice in a sandbox with no network and must write the same bytes
both times, so it copies the image the repository ships.
"""
import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    src = Path(__file__).resolve().parent / "entry.png"
    dst = Path(out_dir) / "entry.png"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    if dst.stat().st_size != src.stat().st_size:
        print(
            f"copy size mismatch: {dst.stat().st_size} != {src.stat().st_size}",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
