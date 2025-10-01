# pysay

A Python cowsay clone for demonstrating uvx.

## Usage

```bash
uvx --from https://github.com/karaage0703/uvx-tools pysay "Hello World"
uvx --from https://github.com/karaage0703/uvx-tools pysay -a dragon "Dragons are cool!"
uvx --from https://github.com/karaage0703/uvx-tools pysay -l
```

## Examples

```bash
# Default cow
uvx --from https://github.com/karaage0703/uvx-tools pysay "Hello from uvx!"

# Use a dragon
uvx --from https://github.com/karaage0703/uvx-tools pysay -a dragon "Roar!"

# Use Tux (Linux penguin)
uvx --from https://github.com/karaage0703/uvx-tools pysay -a tux "I love Linux"

# List available animals
uvx --from https://github.com/karaage0703/uvx-tools pysay -l
```

## Animals

- cow (default)
- dragon
- tux
