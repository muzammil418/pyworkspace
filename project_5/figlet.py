import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    # Check command-line arguments
    if len(sys.argv) == 1:
        font = random.choice(fonts)

    elif len(sys.argv) == 3:
        if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
            font = sys.argv[2]
        else:
            sys.exit("Invalid usage")

    else:
        sys.exit("Invalid usage")

    # Get user input
    text = input("Input: ")

    # Set font and print
    figlet.setFont(font=font)
    print(figlet.renderText(text))


main()