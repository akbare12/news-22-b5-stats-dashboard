#!/usr/bin/env python3
"""Copy program for the news-image-20261122 stats-dashboard entry.

Reproduces entry.png byte-identically: it verifies the bundled image's
size and SHA-256 before copying it to the output directory, so a corrupt
or swapped image fails loudly instead of silently entering a wrong file.
"""
import hashlib
import os
import shutil
import sys

EXPECTED_SHA256 = "4327fa72c740e5437bd785ae6093c5bd0537d7d9b332d340bf07930bf09cf1f5"
EXPECTED_SIZE = 184059
SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(SOURCE, "rb") as fh:
        data = fh.read()
    if len(data) != EXPECTED_SIZE:
        sys.exit("size mismatch: got %d, want %d" % (len(data), EXPECTED_SIZE))
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        sys.exit("sha256 mismatch: got %s, want %s" % (digest, EXPECTED_SHA256))
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    # Verify the copy itself: re-read the target and compare hash and size,
    # so a partial write is caught here instead of downstream.
    with open(target, "rb") as fh:
        copied = fh.read()
    if len(copied) != EXPECTED_SIZE:
        sys.exit("copied size mismatch: got %d, want %d"
                 % (len(copied), EXPECTED_SIZE))
    if hashlib.sha256(copied).hexdigest() != EXPECTED_SHA256:
        sys.exit("copied sha256 mismatch")
    print("wrote %s (%d bytes, sha256 %s)" % (target, len(data), digest))


if __name__ == "__main__":
    main()
