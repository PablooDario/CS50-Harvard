# Program that counts how many lines of code has a program, you have to pass the path of the file within the comand line

import sys

path = sys.argv

if len(path) == 1:
    sys.exit("Too few command-line arguments")
elif len(path) > 2:
    sys.exit("Too many command-line arguments")
elif not path[1].endswith(".py"):
    sys.exit("Not a Python file")

try:
    with open(path[1], "r") as file:
        count = 0
        for line in file:
            line = line.strip()
            if not line.startswith('#') and line != "":
                count +=1
    print(count)
    
except FileNotFoundError:
    sys.exit("File does not exist")