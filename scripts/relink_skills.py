#!/usr/bin/env python3
"""
Portable Skills Relinker for AI-Dev-Team
Audits, repairs, and standardizes skill symlinks to make the ecosystem 100% portable.
- Converts absolute in-repo symlinks to clean relative paths (../repos/..., addyosmani/..., ../plugins/...)
- Dynamically resolves user home directory (~/.gemini/config, ~/.codex) for external native skills
"""

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(ROOT, "skills")
HOME = os.path.expanduser("~")

def relink_all():
    print(f"=== Auditing & Relinking Skills in {SKILLS_DIR} ===")
    if not os.path.isdir(SKILLS_DIR):
        print(f"[FAIL] {SKILLS_DIR} does not exist.")
        return 1

    converted = 0
    repaired_external = 0
    broken_count = 0
    total = 0

    for item in os.listdir(SKILLS_DIR):
        p = os.path.join(SKILLS_DIR, item)
        if not os.path.islink(p):
            continue
        total += 1
        target = os.readlink(p)

        # 1. In-repo absolute links -> make relative
        if ROOT in target:
            rel = os.path.relpath(target, SKILLS_DIR)
            os.unlink(p)
            os.symlink(rel, p)
            converted += 1
            target = rel

        # 2. External links pointing to someone else's /Users/<user>/.gemini
        if "/.gemini/" in target or "/.codex/" in target:
            if not os.path.exists(p):
                # Attempt repair using current user's HOME
                if "/.gemini/" in target:
                    suffix = target.split("/.gemini/")[1]
                    new_target = os.path.join(HOME, ".gemini", suffix)
                elif "/.codex/" in target:
                    suffix = target.split("/.codex/")[1]
                    new_target = os.path.join(HOME, ".codex", suffix)
                else:
                    new_target = None

                if new_target and os.path.exists(new_target):
                    os.unlink(p)
                    os.symlink(new_target, p)
                    repaired_external += 1

        # Check if still broken
        if not os.path.exists(p):
            broken_count += 1

    print(f"[INFO] Total skill symlinks inspected: {total}")
    print(f"[INFO] In-repo symlinks converted to relative: {converted}")
    print(f"[INFO] External symlinks dynamically repaired to $HOME: {repaired_external}")
    if broken_count > 0:
        print(f"[WARN] Remaining broken symlinks: {broken_count}")
    else:
        print(f"[PASS] 0 broken symlinks! All skills properly linked.")
    return 0

if __name__ == "__main__":
    sys.exit(relink_all())
