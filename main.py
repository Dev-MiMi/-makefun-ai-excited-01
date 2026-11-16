"""Publish the bundled Unzip the Storm artwork without runtime dependencies."""

import hashlib
import os
from pathlib import Path
import tempfile


ARTWORK = Path(__file__).resolve().parent / "assets" / "unzip-the-storm.jpg"
EXPECTED_BYTES = 656829
EXPECTED_SHA256 = "308e5ccc42f3791a5d994b0a4910e167caa72f5334e4606f07e087d1549d1551"
MAX_BYTES = 1048576


def validate_artwork(artwork: bytes) -> None:
    """Bind publication to the exact JPEG fully decoded during the build."""
    if len(artwork) != EXPECTED_BYTES or len(artwork) > MAX_BYTES:
        raise ValueError("Bundled artwork has an unexpected size")
    if hashlib.sha256(artwork).hexdigest() != EXPECTED_SHA256:
        raise ValueError("Bundled artwork failed its SHA256 integrity check")


def publish(artwork: bytes, destination: Path) -> None:
    """Finish a private temporary file before atomically replacing the output."""
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb", dir=destination.parent, prefix=".entry-", suffix=".tmp",
            delete=False,
        ) as stream:
            temporary = Path(stream.name)
            stream.write(artwork)
            stream.flush()
            os.fsync(stream.fileno())
        temporary.chmod(0o644)
        os.replace(temporary, destination)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main() -> None:
    artwork = ARTWORK.read_bytes()
    validate_artwork(artwork)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    publish(artwork, destination)


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as error:
        raise SystemExit(f"Could not publish artwork: {error}") from error
