#!/usr/bin/env python3
from pathlib import Path
import zipfile
import datetime

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT.parent / f"voxel-audio-release-{datetime.date.today().isoformat()}.zip"

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.is_file():
            z.write(path, path.relative_to(ROOT.parent))

print(f"Wrote {OUT}")
