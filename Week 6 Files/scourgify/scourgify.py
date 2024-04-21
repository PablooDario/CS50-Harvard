import sys
import csv

def main():
    path = sys.argv
    if len(path) < 3:
        sys.exit("Too few command-line arguments")
    elif len(path) > 3:
        sys.exit("Too many command-line arguments")

    try:
        with open(path[1], 'r') as csvfile:
            names, houses = [], []
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Split the names into last and first
                name = row['name'].split(',')
                # Delete white spaces
                name[1] = name[1].strip()
                names.append(name)
                houses.append(row['house'])
    except :
        sys.exit("Could not read", path[1])

    with open(path[2], 'w', newline='') as csvfile:
        #Create Header for the CSV File
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(houses)):
            writer.writerow({'first': names[i][1], 'last': names[i][0], 'house': houses[i]})


if __name__ == "__main__":
    main()
