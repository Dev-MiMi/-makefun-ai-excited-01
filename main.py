"""Publish the committed Dawn Breaks Free artwork for make.fun."""

import hashlib
import os
from pathlib import Path
import tempfile


ARTWORK = Path(__file__).resolve().parent / "assets" / "dawn-breaks-free.jpg"
EXPECTED_BYTES = 952404
EXPECTED_SHA256 = "3a9573d8e2d18da1ef4d2f7532e2ef15e226beace30c41044990e295a79dfde7"


def main() -> None:
    artwork = ARTWORK.read_bytes()
    if len(artwork) != EXPECTED_BYTES:
        raise ValueError("Artwork integrity check failed: unexpected byte count")
    if hashlib.sha256(artwork).hexdigest() != EXPECTED_SHA256:
        raise ValueError("Artwork integrity check failed: SHA256 mismatch")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    # Stage beside the destination so replacement is atomic on its filesystem.
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb", dir=output_dir, prefix=".entry-", suffix=".tmp", delete=False
        ) as handle:
            temporary = Path(handle.name)
            handle.write(artwork)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, destination)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    print(f"Wrote {len(artwork)} bytes to {destination}")


if __name__ == "__main__":
    main()
