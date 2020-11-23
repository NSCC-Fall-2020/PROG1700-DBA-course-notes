import sys

emojis = {
    'smile': '\U0001F605',
    'santa': '\U0001F385'
}


def show_emoji(name):
    print(emojis[name])


def main():
    if len(sys.argv) > 1:

        if sys.argv[1] == "-h":
            print("Usage: emojis.py <name>")
            sys.exit(0)

        for arg in sys.argv[1:]:
            show_emoji(arg)


if __name__ == "__main__":
    # I am running as a program, not imported
    main()