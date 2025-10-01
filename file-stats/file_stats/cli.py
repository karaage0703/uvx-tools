"""CLI interface for file-stats."""

import sys
import os
from pathlib import Path
from collections import defaultdict
from datetime import datetime


def format_size(size_bytes):
    """Format bytes to human readable format."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} PB"


def analyze_directory(path):
    """Analyze a directory and return statistics."""
    stats = {
        "total_files": 0,
        "total_dirs": 0,
        "total_size": 0,
        "extensions": defaultdict(lambda: {"count": 0, "size": 0}),
        "largest_files": [],
    }

    try:
        for root, dirs, files in os.walk(path):
            stats["total_dirs"] += len(dirs)

            for file in files:
                file_path = Path(root) / file
                try:
                    file_size = file_path.stat().st_size
                    stats["total_files"] += 1
                    stats["total_size"] += file_size

                    ext = file_path.suffix.lower() or "(no extension)"
                    stats["extensions"][ext]["count"] += 1
                    stats["extensions"][ext]["size"] += file_size

                    stats["largest_files"].append((str(file_path), file_size))
                except (OSError, PermissionError):
                    pass

        # Sort and limit largest files
        stats["largest_files"].sort(key=lambda x: x[1], reverse=True)
        stats["largest_files"] = stats["largest_files"][:10]

    except PermissionError:
        print(f"Error: Permission denied accessing {path}")
        sys.exit(1)

    return stats


def print_stats(path, stats):
    """Print formatted statistics."""
    print(f"\n📊 File Statistics for: {path}")
    print("=" * 60)

    print(f"\n📁 Overview:")
    print(f"   Files: {stats['total_files']:,}")
    print(f"   Directories: {stats['total_dirs']:,}")
    print(f"   Total Size: {format_size(stats['total_size'])}")

    if stats["extensions"]:
        print(f"\n📄 File Types:")
        sorted_exts = sorted(
            stats["extensions"].items(), key=lambda x: x[1]["size"], reverse=True
        )
        for ext, data in sorted_exts[:10]:
            print(
                f"   {ext:20} {data['count']:>6} files  {format_size(data['size']):>12}"
            )

    if stats["largest_files"]:
        print(f"\n🔝 Top 10 Largest Files:")
        for file_path, size in stats["largest_files"]:
            filename = Path(file_path).name
            print(f"   {format_size(size):>12}  {filename}")

    print("\n" + "=" * 60)


def main():
    """Main entry point for file-stats."""
    args = sys.argv[1:]

    if not args or args[0] in ("-h", "--help"):
        print("Usage: file-stats [PATH]")
        print("\nAnalyze files and directories.")
        print("\nOptions:")
        print("  -h, --help    Show this help")
        print("\nExamples:")
        print("  file-stats .")
        print("  file-stats /path/to/directory")
        sys.exit(0 if not args else 1)

    path = args[0]

    if not os.path.exists(path):
        print(f"Error: Path '{path}' does not exist")
        sys.exit(1)

    if os.path.isfile(path):
        file_path = Path(path)
        size = file_path.stat().st_size
        mtime = datetime.fromtimestamp(file_path.stat().st_mtime)

        print(f"\n📄 File Information: {file_path.name}")
        print("=" * 60)
        print(f"   Path: {file_path.absolute()}")
        print(f"   Size: {format_size(size)}")
        print(f"   Modified: {mtime.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"   Extension: {file_path.suffix or '(none)'}")
        print("=" * 60 + "\n")
    else:
        stats = analyze_directory(path)
        print_stats(path, stats)


if __name__ == "__main__":
    main()
