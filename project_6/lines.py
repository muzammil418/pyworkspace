import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py file.py")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(filename, "r") as file:
            count = 0

            for line in file:
                line = line.strip()

                if line == "":
                    continue

                if line.startswith("#"):
                    continue

                count += 1

        print(count)

    except FileNotFoundError:
        sys.exit("File does not exist")


main()