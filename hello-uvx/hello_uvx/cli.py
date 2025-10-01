"""CLI interface for hello-uvx."""

import sys
from datetime import datetime


def main():
    """Main entry point for hello-uvx."""
    args = sys.argv[1:]

    if not args:
        name = "World"
    else:
        name = " ".join(args)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"╔═══════════════════════════════════╗")
    print(f"║  Hello, {name}!".ljust(36) + "║")
    print(f"║  Time: {now}".ljust(36) + "║")
    print(f"║  Running via uvx ✨".ljust(36) + "║")
    print(f"╚═══════════════════════════════════╝")


if __name__ == "__main__":
    main()
