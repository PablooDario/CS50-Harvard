# Etcetera

## Content Table

- [Sets](#Sets)
- [Maps](#map)
- [List & Dictionary Comprehenssion](#list--dictionary-comprehension)
- [Global Variables](#global-variables)
- [Constants](#constants)
- [Type Hints](#type-hints)
- [DocStrings](#docstrings)
- [ArgParser](#argparse)
- [Unpacking](#unpacking)
- [Args and kwargs](#args-and-kwargs)
- [Filter](#filter)
- [Generators and Iterators](#generators-and-iterators)

In this lesson, we will be focusing upon many of the “et cetera” items not previously discussed

## Sets

In math, a set would be considered a set of numbers without any duplicates. It turns out we can use the built-in set features to eliminate duplicates.

```Python 
hunters = [
    {"name": "Killua", "type": "Transmutation"},
    {"name": "Gon", "type": "Enhancement"},
    {"name": "Leorio", "type": "Emission"},
    {"name": "Kurapika", "type": "Conjuration"},
    {"name": "Hisoka", "type": "Transmutation"},
]

types = set()
for hunter in hunters:
    types.add(hunter["type"])

for type in sorted(types):
    print(type)
```

## Global Variables

In other programming languages, there is the notion of global variables that are accessible to any function. To interact with a global variable inside a function, the solution is to use the global keyword

```Python
balance = 0


def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n):
    global balance
    balance += n


def withdraw(n):
    global balance
    balance -= n


if __name__ == "__main__":
    main()
```

Utilizing our powers from our experience with object-oriented programming, we can modify our code to use a class instead of a global. Generally speaking, global variables should be **used quite sparingly.**

## Constants

Some languages allow you to create variables that are unchangeable, called “constants”. Constants allow one to program defensively and reduce the opportunities for important values to be altered.

Constants are typically denoted by capital variable names and are placed at the top of our code. Though this looks like a constant, in reality, Python actually has no mechanism to prevent us from changing that value within our code! Instead, you’re on the honor system: if a variable name is written in all caps, just don’t change it!

```python
HELLO = 2
for _ in range(HELLO):
    print("Hello World")
```


One can create a class “constant”, now in quotes because we know Python doesn’t quite support “constants”.

```Python
class Cat:
    helloS = 3

    def hello(self):
        for _ in range(Cat.helloS):
            print("hello")


cat = Cat()
cat.hello()
```

## Type Hints

In other programming languages, one expresses **explicitly what variable type** you want to use, but **Python does not require the explicit declaration of types.** Nevertheless, it’s good practice need to ensure all of your variables are of the right type.

`mypy` is a program that can help you test to make sure all your variables are of the right type.

```python
def hello(n: int) -> str:
    return "hello\n" * n


number: int = int(input("Number: "))
hellos: str = hello(number)
print(hellos, end="")
```

## DocStrings

A standard way of commenting your function’s purpose is to use a **docstring**. You can use docstrings to **standardize how you document the features of a function.**

```python
def hello(n):
    """
    hello n times.

    :param n: Number of times to print hello
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n hello's, one per line
    :rtype: str
    """
    return "hello\n" * n


number = int(input("Number: "))
hellos = hello(number)
print(hellos, end="")
```

Established tools, such as `Sphinx`, can be used to **parse docstrings and automatically create documentation** for us in the form of web pages and PDF files such that you can publish and share with others.

## Argparse

`argparse` is a library that **handles all the parsing** of complicated strings of **command-line arguments.**

We can also program more cleanly, such that our user can get some information about the proper usage of our code when they fail to use the program correctly. 

```python
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")
```

## Unpacking

We can pass element by element of a list to a function, but this could be very vebose, so we can **pass the whole list** and let python take **care of distributing its elements**; we can do this with a `*`, that unpacks the sequence of the list and passes in each of its individual elements to the function.

```python 
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

print(total(*coins), "Knuts")
```

If we also want to pass the **names and the values of each element**, we can use a dictionary and then unpackig to eploit each of it's elements with `**`.
```python
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "Knuts")
```
## ARGS and KWARGS

Recall the print documentation:

`print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`

`args` are positional arguments, such as those we provide to print like print `("Hello", "World")`
`kwargs` are named arguments, or **“keyword arguments”**, such as those we provide to print like `print(end="")`

As we see in the prototype for the print function above, we can tell our function to expect a presently unknown number positional arguments. 

```python
def f(*args, **kwargs):
    print("Positional:", args)

f(100, 50, 25)
```

We can even pass in named arguments.
```python 
def f(*args, **kwargs):
    print("Named:", kwargs)

f(galleons=100, sickles=50, knuts=25)
```

## Map

Early on, we began with procedural programming, where just to illustrate we can return words in upper case.

```python
def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


if __name__ == "__main__":
    main()
```

`map` allows you to map a function to a sequence of values. 

```python
def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()
```

Notice how map takes two arguments. First, it takes a function we want applied to every element of a list. Second, it takes that list itself, to which we’ll apply the aforementioned function. Hence, all words in words will be handed to the str.upper function and returned to uppercased.

## List & Dictionary Comprehension

List comprehensions allow you to **create a list on the fly** in one elegant one-line. We can implement the above example of map with list comprehension: 

```python
def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = [arg.upper() for arg in words]
    print(*uppercased)


if __name__ == "__main__":
    main()
```

We also can create a list of dcitionaries and use condtionals

```python
squares_even_numbers = {
    x: x**2 for x in range(5) if x % 2 == 0
    }
print(squares_even_number)
```

We can apply the same idea behind list comprehensions to dictionaries.

```python
students = ["Gon", "Killua", "Kurapika"]

hunters = {student: "Hunter!" for student in students}

print(hunters)
```

## Filter

Using Python’s filter function allows us to return a **subset of a sequence** for which a **certain condition is true**.

```python
hunters = [
    {"name": "Killua", "type": "Transmutation"},
    {"name": "Gon", "type": "Enhancement"},
    {"name": "Kurapika", "type": "Conjuration"},
    {"name": "Hisoka", "type": "Transmutation"},
]

def is_Transmutation(h):
    return h["type"] == "Transmutation"


transmutators = filter(is_Transmutation, hunters)
# transmutators = filter(lambda s: s["type"] == "Transmutation", hunters)

for transmutator in sorted(transmutators, key=lambda s: s["name"]):
    print(transmutator["name"])
```

## Generators and Iterators

In Python, there is a way to **protect** against your system **running out of resources** the problems they are addressing become too large.

```python
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock


if __name__ == "__main__":
    main()
```
Executing our code, you might try different numbers of sheep such as 10, 1000, and 10000. What if you asked for 1000000 sheep, **your program might completely hang or crash.** Because you have attempted to **generate a massive list of sheep, your computer may be struggling to complete the computation.**

The `yield` generator can solve this problem by **returning a small bit of the results at a time.** 

```python
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    main()
```
