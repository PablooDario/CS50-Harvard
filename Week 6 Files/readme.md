# Files I/O

`open` is a functionality built into Python that allows you to open a file and utilize it in your program. The open function allows you to open a file such that you can read from it or write to it.

```Python
name = input("What's your name? ")

file = open("names.txt", "w")
file.write(name)
file.close()
```

Ideally, we want to be able to append each of our names to the file, so we have to switch the mode form *write* to *append*

```Python
file = open("names.txt", "a")
```

## With

But there is a another way to open a file that help us to automatically close the file and it is a more readable way and that is the keyword `with`

```Python
name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
```

Now if we want to read our file, we have to switch from the *writing* mode to *reading*

```Python
with open("names.txt", "r") as file:
    for line in file:
        # .rstrip() help us to delete the '\n' character that has each line
        print("hello,", line.rstrip())
```

If we want to store all the content in a list we can do the following:

```Python
with open("names.txt", "r") as file:
    lines = file.readlines()
```

## CSV

Python’s built-in csv library comes with an object called a reader. As the name suggests, we can use a reader to read our CSV

```Python
import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "home": row[1]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
```

We can modify our code to use a part of the csv library called a DictReader to treat our CSV file with even more flexibilty, this will only work as long as the person designing the CSV file has inputted the correct header information on the first line, so we can access that information using our program.

```Python
import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        #students.append({"name": row["name"], "home": row["home"]})
        students.append(row)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")
```
We also can write in our CSV file

```Python
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
```