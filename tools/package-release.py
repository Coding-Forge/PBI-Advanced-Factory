#!/usr/bin/env python3
"""Package student-facing release bundles for the Power BI Advanced Factory workshop.

Builds a zip of only the files a learner needs for a given delivery track:

  three-day  -> Modules 1-7 (matches docs/three-day-training-agenda.md)
  full       -> Modules 1-12 (the complete progressive workshop)

Usage:
    python tools/package-release.py --track three-day --version 1.0.0
    python tools/package-release.py --track full --version 1.0.0

Output is written to dist/<zip-name>.zip. This script only reads from the
repo; it never modifies source files.
"""
from __future__ import annotations

import argparse
import fnmatch
import shutil
import sys
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DIST_DIR = REPO_ROOT / "dist"

THREE_DAY_MODULES = [f"{i:02d}-" for i in range(1, 8)]  # 01 .. 07
FULL_MODULES = [f"{i:02d}-" for i in range(1, 12)]  # 01 .. 11 (+ 12-capstone handled separately)

# Docs that are shared/introductory and relevant regardless of track.
COMMON_DOCS = [
    "docs/environment-setup-guide.md",
    "docs/troubleshooting-guide.md",
    "docs/learner-workbook.md",
    "docs/lab-manual.md",
    "docs/knowledge-checks-and-answer-keys.md",
    "docs/data-dictionary.md",
    "docs/gov-delivery-notes.md",
    "docs/commercial-delivery-notes.md",
]

THREE_DAY_DOCS = COMMON_DOCS + ["docs/three-day-training-agenda.md"]
FULL_DOCS = COMMON_DOCS + [
    "docs/three-day-training-agenda.md",
    "docs/advanced-powerbi-training-outline.md",
    "docs/delivery-paths.md",
]

# Jeopardy review games and PDF/Web/Source subfolders are filtered by module prefix.
JEOPARDY_COMMON = ["index.html", "jeopardy.css", "jeopardy.js", "data"]


def module_prefixes(track: str) -> list[str]:
    return THREE_DAY_MODULES if track == "three-day" else FULL_MODULES + ["12-capstone"]


def matches_module(name: str, prefixes: list[str]) -> bool:
    return any(name.startswith(p) for p in prefixes)


def copy_tree_filtered(src: Path, dst: Path, keep_names) -> None:
    """Copy immediate children of src into dst, keeping only entries where keep_names(name) is True."""
    if not src.exists():
        return
    dst.mkdir(parents=True, exist_ok=True)
    for child in sorted(src.iterdir()):
        if keep_names(child.name):
            target = dst / child.name
            if child.is_dir():
                shutil.copytree(child, target, dirs_exist_ok=True)
            else:
                shutil.copy2(child, target)


def build_readme(track: str, version: str) -> str:
    if track == "three-day":
        return f"""# Power BI Advanced Factory - Three-Day Delivery (v{version})

This package contains the student materials for the **three-day delivery**
of the Power BI Advanced Factory workshop, covering Modules 1-7:

1. Advanced Semantic Modeling
2. Advanced DAX
3. Advanced Power Query and Data Transformation
4. Advanced Report Design and User Experience
5. Performance Optimization
6. Advanced Analytics and AI-Assisted Insights
7. Security Design

See `docs/three-day-training-agenda.md` for the hour-by-hour agenda.

## What's included

- `Student/Labs/Source/01-07-*` - starter and solution PBIP projects for each lab
- `Student/Labs/PDF/01-07-*.pdf` - printable lab manuals
- `Student/Labs/Web/*` - self-contained HTML lab site (open `Web/index.html`)
- `Student/Labs/Web/jeopardy/*` - optional review games for Labs 1-7
- `pbi-stepwise/` - a single semantic model/report built up incrementally,
  one exercise at a time, across Labs 1-7. Use this as a reference to see
  exactly what changes after each exercise (check the git history in the
  full repository for a commit-by-commit walkthrough). This reference does
  **not** cover Modules 8-12.
- `data/` - shared sample datasets used across the labs
- `docs/` - environment setup, troubleshooting, learner workbook, lab
  manual, knowledge checks/answer keys, data dictionary, and Gov/commercial
  delivery notes

## Not included in this package

Modules 8-12 (Service Enterprise Deployment, Monitoring/Governance,
Premium/Fabric/Capacity, Automation/DevOps, and the Capstone) are part of
the full progressive workshop. Ask your instructor about the **full
delivery** release if you want to continue past Module 7.
"""
    return f"""# Power BI Advanced Factory - Full Delivery (v{version})

This package contains the complete student materials for all 11 modules
plus the capstone lab. See `docs/advanced-powerbi-training-outline.md` and
`docs/delivery-paths.md` for the full curriculum and suggested delivery
tracks.
"""


def build(track: str, version: str) -> Path:
    staging = DIST_DIR / f"_staging-{track}"
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    prefixes = module_prefixes(track)

    # README
    (staging / "README.md").write_text(build_readme(track, version), encoding="utf-8")

    # docs
    doc_list = THREE_DAY_DOCS if track == "three-day" else FULL_DOCS
    for rel in doc_list:
        src = REPO_ROOT / rel
        if src.exists():
            dst = staging / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

    # data (shared across all labs)
    data_src = REPO_ROOT / "data"
    if data_src.exists():
        shutil.copytree(data_src, staging / "data", dirs_exist_ok=True)

    # Student/Labs/Source/<module>/**
    source_root = REPO_ROOT / "Student" / "Labs" / "Source"
    copy_tree_filtered(
        source_root,
        staging / "Student" / "Labs" / "Source",
        lambda name: name == "README.md" or matches_module(name, prefixes),
    )

    # Student/Labs/PDF/<module>.pdf
    pdf_root = REPO_ROOT / "Student" / "Labs" / "PDF"
    copy_tree_filtered(
        pdf_root,
        staging / "Student" / "Labs" / "PDF",
        lambda name: name == "README.md" or matches_module(Path(name).stem + "-", prefixes),
    )

    # Student/Labs/Web
    web_root = REPO_ROOT / "Student" / "Labs" / "Web"
    web_dst = staging / "Student" / "Labs" / "Web"
    web_dst.mkdir(parents=True, exist_ok=True)
    for child in sorted(web_root.iterdir()):
        if child.name == "jeopardy":
            continue  # handled separately below
        if child.is_dir():
            shutil.copytree(child, web_dst / child.name, dirs_exist_ok=True)
        elif child.suffix == ".html" and child.stem not in ("index",):
            if matches_module(Path(child.name).stem + "-", prefixes):
                shutil.copy2(child, web_dst / child.name)
        else:
            shutil.copy2(child, web_dst / child.name)

    jeopardy_src = web_root / "jeopardy"
    if jeopardy_src.exists():
        jeopardy_dst = web_dst / "jeopardy"
        jeopardy_dst.mkdir(parents=True, exist_ok=True)

        def keep_jeopardy_file(name: str) -> bool:
            if track == "full":
                return True
            if name in ("final-review.html", "final-review.js"):
                return False
            m = fnmatch.fnmatch(name, "lab*.html") or fnmatch.fnmatch(name, "lab*.js")
            if not m:
                return True  # shared assets like jeopardy.css/js
            module_num = Path(name).stem.replace("lab", "")
            return matches_module(f"{module_num}-", prefixes)

        for child in sorted(jeopardy_src.iterdir()):
            if child.name in JEOPARDY_COMMON and child.is_dir():
                # "data" subfolder holds per-lab question sets; filter its contents too
                data_dst = jeopardy_dst / child.name
                data_dst.mkdir(parents=True, exist_ok=True)
                for sub in sorted(child.iterdir()):
                    if keep_jeopardy_file(sub.name):
                        shutil.copy2(sub, data_dst / sub.name)
            elif child.name in JEOPARDY_COMMON:
                shutil.copy2(child, jeopardy_dst / child.name)
            elif keep_jeopardy_file(child.name):
                shutil.copy2(child, jeopardy_dst / child.name)

    # pbi-stepwise reference (Labs 1-7 cumulative build) - always relevant up to module 7
    stepwise_src = REPO_ROOT / "pbi-stepwise"
    if stepwise_src.exists():
        shutil.copytree(stepwise_src, staging / "pbi-stepwise", dirs_exist_ok=True)

    # pbi-complete (fully completed reference solution) - full delivery only
    if track == "full":
        complete_src = REPO_ROOT / "pbi-complete"
        if complete_src.exists():
            shutil.copytree(complete_src, staging / "pbi-complete", dirs_exist_ok=True)

    # Zip it up
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    zip_name = f"PowerBI-Advanced-Factory-{'ThreeDay' if track == 'three-day' else 'Full'}-v{version}"
    zip_path = DIST_DIR / f"{zip_name}.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in staging.rglob("*"):
            if file.is_file():
                zf.write(file, arcname=str(Path(zip_name) / file.relative_to(staging)))

    shutil.rmtree(staging)
    return zip_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--track", choices=["three-day", "full"], required=True)
    parser.add_argument("--version", required=True, help="Release version, e.g. 1.0.0")
    args = parser.parse_args()

    zip_path = build(args.track, args.version)
    print(f"Wrote {zip_path} ({zip_path.stat().st_size / 1024:.0f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
