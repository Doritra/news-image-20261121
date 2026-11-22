"""News-image entry for 21 November 2026, v3 (final edition).

The repository ships the finished front page as entry.png (37 stories
from Saturday 21 November 2026, one 1024x1024 picture: bigger 19px
section headlines and more air than v2's dense 17px layout, lead story
Iran's strikes on US positions in Bahrain); this program copies it to
the output directory, byte for byte, with no network use. Outside the
grader, MAKEFUN_OUTPUT_DIR stands in for /output.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    # The grader mounts a writable /output; locally MAKEFUN_OUTPUT_DIR overrides it.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).resolve().parent / "entry.png"
    shutil.copyfile(source, out_dir / "entry.png")  # byte-for-byte copy


if __name__ == "__main__":
    main()
