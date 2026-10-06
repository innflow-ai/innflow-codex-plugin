#!/usr/bin/env python3
"""Package only the Innflow plugin and its standalone marketplace catalog."""

import argparse
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    plugin = root / "plugins/innflow"
    # Explicit allowlist prevents future local files or credentials entering releases.
    files = [
        "plugin.json",
        "mcp.json",
        "README.md",
        "assets/icon.png",
        "skills/innflow-workflows/SKILL.md",
    ]
    manifest = json.loads((plugin / "plugin.json").read_text())
    catalog = json.loads((root / ".agents/plugins/marketplace.json").read_text())
    entry = next(item for item in catalog["plugins"] if item["name"] == manifest["name"])
    standalone_catalog = {**catalog, "plugins": [entry]}
    # Read everything first, so a missing file cannot leave a partial release.
    contents = [(f"plugins/innflow/{name}", (plugin / name).read_bytes()) for name in files]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(args.output, "w", compression=ZIP_DEFLATED) as archive:
        archive.writestr(".agents/plugins/marketplace.json", json.dumps(standalone_catalog, indent=2) + "\n")
        for name, content in contents:
            archive.writestr(name, content)
    print(f"Packaged {manifest['name']} {manifest['version']}: {args.output}")


if __name__ == "__main__":
    main()
