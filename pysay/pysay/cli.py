"""CLI interface for pysay."""

import sys


ANIMALS = {
    "cow": r"""
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
    """,
    "dragon": r"""
        \                    / \  //\
         \    |\___/|      /   \//  \\
              /0  0  \__  /    //  | \ \
             /     /  \/_/    //   |  \  \
             @_^_@'/   \/_   //    |   \   \
             //_^_/     \/_ //     |    \    \
          ( //) |        \///      |     \     \
        ( / /) _|_ /   )  //       |      \     _\
      ( // /) '/,_ _ _/  ( ; -.    |    _ _\.-~        .-~~~^-.
    (( / / )) ,-{        _      `-.|.-~-.           .~         `.
   (( // / ))  '/\      /                 ~-. _ .-~      .-~^-.  \
   (( /// ))      `.   {            }                   /      \  \
    (( / ))     .----~-.\        \-'                 .~         \  `. \^-.
               ///.----..>        \             _ -~             `.  ^-`  ^-_
                 ///-._ _ _ _ _ _ _}^ - - - - ~                     ~-- ,.-~
    """,
    "tux": r"""
        \
         \
            .--.
           |o_o |
           |:_/ |
          //   \ \
         (|     | )
        /'\_   _/`\
        \___)=(___/
    """,
}


def create_bubble(text, width=40):
    """Create a speech bubble around text."""
    lines = []
    words = text.split()
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) > width:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_length = len(word)
        else:
            current_line.append(word)
            current_length += len(word)

    if current_line:
        lines.append(" ".join(current_line))

    if not lines:
        lines = [""]

    max_len = max(len(line) for line in lines) if lines else 0
    border = " " + "-" * (max_len + 2)

    result = [border]
    if len(lines) == 1:
        result.append(f"< {lines[0].ljust(max_len)} >")
    else:
        for i, line in enumerate(lines):
            if i == 0:
                result.append(f"/ {line.ljust(max_len)} \\")
            elif i == len(lines) - 1:
                result.append(f"\\ {line.ljust(max_len)} /")
            else:
                result.append(f"| {line.ljust(max_len)} |")
    result.append(border)

    return "\n".join(result)


def main():
    """Main entry point for pysay."""
    args = sys.argv[1:]

    animal = "cow"
    text = "Hello from pysay!"

    # Parse arguments
    i = 0
    while i < len(args):
        if args[i] in ("-a", "--animal"):
            if i + 1 < len(args):
                animal = args[i + 1]
                i += 2
            else:
                print("Error: --animal requires an argument")
                sys.exit(1)
        elif args[i] in ("-l", "--list"):
            print("Available animals:")
            for name in ANIMALS:
                print(f"  - {name}")
            sys.exit(0)
        elif args[i] in ("-h", "--help"):
            print("Usage: pysay [OPTIONS] [TEXT]")
            print("\nOptions:")
            print("  -a, --animal ANIMAL  Choose animal (cow, dragon, tux)")
            print("  -l, --list           List available animals")
            print("  -h, --help           Show this help")
            sys.exit(0)
        else:
            text = " ".join(args[i:])
            break

    if animal not in ANIMALS:
        print(f"Error: Unknown animal '{animal}'. Use -l to list available animals.")
        sys.exit(1)

    print(create_bubble(text))
    print(ANIMALS[animal])


if __name__ == "__main__":
    main()
