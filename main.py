#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message - make.fun bounty entry.

Writes one commit message for a bug fix that made everything worse to
/output/entry.txt (37 characters, one line), the artifact the house
judge reads two at a time.
"""
import os

LINE = "fix: off-by-one error, now off by two"
MAX_CHARS = 100  # the sealed gate refuses entry.txt over 100 characters

def main():
    if not 1 <= len(LINE) <= MAX_CHARS or LINE.strip() != LINE or "\n" in LINE:
        raise SystemExit(f"entry line must be one line of 1-{MAX_CHARS} chars, got {len(LINE)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    print(LINE)

if __name__ == "__main__":
    main()
