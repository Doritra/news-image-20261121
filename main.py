"""News-image entry for 21 November 2026.

The repository ships the finished front page as entry.png; this program
copies it to the output directory, byte for byte, with no network use.
Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    # The grader mounts a writable /output; locally MAKEFUN_OUTPUT_DIR overrides it.
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).resolve().parent / "entry.png"
    shutil.copyfile(source, output_dir / "entry.png")


if __name__ == "__main__":
    main()
