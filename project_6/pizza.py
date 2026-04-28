import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) != 2:
        sys.exit("usage: python pizza.py file.csv")

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("not a csv file")

    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)

            headers = next(reader)
            table = []

            for row in reader:
                table.append(row)

            print(tabulate(table, headers, tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


main()