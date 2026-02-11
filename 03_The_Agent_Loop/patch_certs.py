#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# ///
"""Patch certifi CA bundles with a corporate certificate (e.g., Zscaler).

Discovers .venv directories and appends the certificate to certifi's CA bundle,
enabling HTTPS requests to work behind corporate proxies.
"""

import argparse
from pathlib import Path


def find_certifi_bundles(start_path: Path) -> list[Path]:
    """Find all certifi cacert.pem files in .venv directories."""
    bundles = []
    for venv in start_path.rglob(".venv"):
        if not venv.is_dir():
            continue
        # Look for certifi in both possible locations
        for pattern in [
            "lib/python*/site-packages/certifi/cacert.pem",
            "Lib/site-packages/certifi/cacert.pem",  # Windows
        ]:
            bundles.extend(venv.glob(pattern))
    return bundles


def prompt_for_cert_path() -> Path:
    """Prompt user for certificate path."""
    print("No certificate path provided.")
    while True:
        cert_input = input("Enter path to certificate file: ").strip()
        if not cert_input:
            print("Path cannot be empty.")
            continue
        cert_path = Path(cert_input).expanduser().resolve()
        if cert_path.exists():
            return cert_path
        print(f"File not found: {cert_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Patch certifi CA bundles with a corporate certificate (e.g., Zscaler).",
        epilog="""
Examples:
  %(prog)s -c certs/zscaler.crt
  %(prog)s -c ~/certs/corporate.crt -d /path/to/projects
  %(prog)s  # Interactive mode, prompts for cert path
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "-c", "--cert",
        metavar="PATH",
        help="Path to the certificate file to add (e.g., zscaler.crt)",
    )
    parser.add_argument(
        "-d", "--dir",
        metavar="PATH",
        default=".",
        help="Directory to search for .venv folders (default: current directory)",
    )
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Only show summary, not individual files",
    )

    args = parser.parse_args()

    # Get certificate path
    if args.cert:
        cert_path = Path(args.cert).expanduser().resolve()
        if not cert_path.exists():
            parser.error(f"Certificate not found: {cert_path}")
    else:
        cert_path = prompt_for_cert_path()

    # Get search directory
    search_dir = Path(args.dir).expanduser().resolve()
    if not search_dir.is_dir():
        parser.error(f"Not a directory: {search_dir}")

    if not args.quiet:
        print(f"Certificate: {cert_path}")
        print(f"Searching in: {search_dir}")
        print()

    cert_content = cert_path.read_text()

    # Find all certifi bundles
    bundles = find_certifi_bundles(search_dir)

    if not bundles:
        print("No .venv directories with certifi found")
        return

    patched = 0
    skipped = 0

    for bundle in bundles:
        current_content = bundle.read_text()

        # Check if already patched (look for cert content)
        if cert_content.strip() in current_content:
            if not args.quiet:
                print(f"Already patched: {bundle}")
            skipped += 1
            continue

        # Append certificate
        with open(bundle, "a") as f:
            f.write(f"\n# Added by patch_certs.py from {cert_path.name}\n")
            f.write(cert_content)

        if not args.quiet:
            print(f"Patched: {bundle}")
        patched += 1

    print(f"\nDone: {patched} patched, {skipped} already patched")


if __name__ == "__main__":
    # main()
    from langgraph.prebuilt import ToolNode
    ToolNode
