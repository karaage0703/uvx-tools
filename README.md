# UVX Tools Collection

uvx で動作する Python CLI ツール集

## ツール一覧

### 1. hello-uvx
シンプルな Hello World ツール

```bash
uvx --from git+https://github.com/karaage0703/uvx-tools hello-uvx
uvx --from git+https://github.com/karaage0703/uvx-tools hello-uvx 'Your Name'
```

### 2. pysay
cowsay クローン - 動物が喋るツール

```bash
uvx --from git+https://github.com/karaage0703/uvx-tools pysay 'Hello World'
uvx --from git+https://github.com/karaage0703/uvx-tools pysay -a dragon 'Dragons are cool'
uvx --from git+https://github.com/karaage0703/uvx-tools pysay -l  # 利用可能な動物一覧
```

### 3. file-stats
ファイル・ディレクトリ分析ツール

```bash
uvx --from git+https://github.com/karaage0703/uvx-tools file-stats .
uvx --from git+https://github.com/karaage0703/uvx-tools file-stats /path/to/directory
```

## 使い方

以下のコマンドで直接実行できます:

```bash
uvx --from git+https://github.com/karaage0703/uvx-tools <command-name> [args]
```

## 開発

各ツールは独立したPythonパッケージです:

- `pyproject.toml`: プロジェクト設定
- `<tool>/__init__.py`: パッケージ初期化
- `<tool>/cli.py`: CLI実装
- `README.md`: ツール固有のドキュメント

## 動作確認

```bash
# hello-uvx
uvx --from git+https://github.com/karaage0703/uvx-tools hello-uvx 'Test'

# pysay
uvx --from git+https://github.com/karaage0703/uvx-tools pysay -a tux 'Hello from Tux'

# file-stats
uvx --from git+https://github.com/karaage0703/uvx-tools file-stats .
```
