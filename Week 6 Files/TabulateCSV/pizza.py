import sys
from tabulate import tabulate
import csv

def main():
    path = sys.argv
    if len(path) < 2:
        sys.exit("Too few command-line arguments")
    elif len(path) > 2:
        sys.exit("Too many command-line arguments")
    elif not path[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(path[1], 'r') as csvfile:
            lines = []
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                lines.append(row)

            print(tabulate(lines, headers="firstrow", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()