# file-stats

A file and directory analyzer for demonstrating uvx.

## Usage

```bash
uvx --from https://github.com/karaage0703/uvx-tools file-stats .
uvx --from https://github.com/karaage0703/uvx-tools file-stats /path/to/directory
uvx --from https://github.com/karaage0703/uvx-tools file-stats /path/to/file.txt
```

## Features

- 📊 Total file and directory counts
- 💾 Total size calculation
- 📄 File type distribution
- 🔝 Top 10 largest files
- 📁 Single file information

## Examples

```bash
# Analyze current directory
uvx --from https://github.com/karaage0703/uvx-tools file-stats .

# Analyze specific directory
uvx --from https://github.com/karaage0703/uvx-tools file-stats /Users/yourname/Documents

# Analyze single file
uvx --from https://github.com/karaage0703/uvx-tools file-stats README.md
```

## Output Example

```
📊 File Statistics for: .
============================================================

📁 Overview:
   Files: 1,234
   Directories: 45
   Total Size: 12.34 MB

📄 File Types:
   .py                    456 files      8.90 MB
   .md                     89 files      1.23 MB
   .txt                    123 files     890.45 KB
   ...

🔝 Top 10 Largest Files:
       2.34 MB  large_file.dat
       1.89 MB  video.mp4
       987.65 KB  archive.zip
   ...

============================================================
```
