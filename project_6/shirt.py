import sys
from PIL import Image, ImageOps

def main():
    valid_exist = (".jpg", ".jpeg", ".png")

    if len(sys.argv) != 3:
        sys.exit("Wrong number of command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    input_exist = input_file.lower().endswith(valid_exist)
    output_exist = output_file.lower().endswith(valid_exist)

    if not input_exist or not output_exist:
        sys.exit("Input and output have different extensions")


    try:
        with Image.open(input_file) as img:
            shirt = Image.open("shirt.png")

            img = ImageOps.fit(img, shirt.size)

            img.paste(shirt, shirt)

            img.save(output_file)           


    except FileNotFoundError:
        sys.exit("Input file does not exist")



main()