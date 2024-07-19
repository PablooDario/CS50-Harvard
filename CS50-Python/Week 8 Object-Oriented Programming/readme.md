# Object-Oriented Programming 

There are different **paradigms of programming**. We will start recognizing patterns with experience. Up until now, we have worked **procedurally step-by-step**.

**Object-oriented programming** (OOP) is a compelling solution to programming-related problems.

## Classes

**Classes** are a way by which, in object-oriented programming, we can **create our own type of data** and give them names. A class is like a **mold for a type of data** where we can invent our own data type and give them a name.

Example of Modular Programming:

```Python
def main():
    # student is a dictionary
    student = get_student()
    print(f"{student['name']} from {student['school']}")

def get_student():
    name = input("Name: ")
    school = input("School: ")
    return {"name": name, "School": school}

if __name__ == "__main__":
    main()
```

We can convert the example below into OOP paradigm

```Python 
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school

def main():
    # student is an instance of the class Student
    student = get_student()
    print(f"{student.name} from {student.school}")

def get_student():
    name = input("Name: ")
    school = input("School: ")
    student = Student(name, school)
    return student

if __name__ == "__main__":
    main()
```

Any time you **create a class** and you utilize that *blueprint* to create something, you create what is called an **“object”** or an **“instance”**. In the case of the code below, *student* is an object.

Object-oriented program **encourages** to **encapusulate** all the functionality of a class within the class definition.

### Raise

we can create our **own exceptions** that alerts the programmer to a potential ^^ created by the user called raise. **We  can raise ValueError** with a specific error message. Like in the following code:

```Python 
class Student:
    def __init__(self, name, school):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.school = school
```

### Stringify 

Python allows us to create a specific function by which provides a means by which a class is returned when called. We just have to create a built-in method that comes with Python classes and write how we want to print our class and it's attributes.

```Python 
class Student:
    def __init__(self, name, school):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.school = school

    def __str__(self):
        return f"{self.name} from {self.school}"

def main():
    student = Student("Pablo", "Stanford")
    print(student)

if __name__ == "__main__":
    main()
```

## Decorators 
Properties can be utilized to harden our code. In Python, we define properties using function “decorators”, which begin with @

``` Python 
class Student:
    def __init__(self, name, school):
        if not name:
            raise ValueError("Invalid name")
        self.name = name
        self.school = school

    # Getter for school
    @property
    def school(self):
        return self._school

    # Setter for school
    @school.setter
    def school(self, school):
        if not school:
            raise ValueError("Missing school")
        self._school = school


def main():
    student = get_student()


def get_student():
    name = input("Name: ")
    school = input("school: ")
    return Student(name, school)


if __name__ == "__main__":
    main()
```
We defined **school** as a **property** of our **class** by writting *@property* above the function called **school**. Now with school as a property, we gain the ability to define how some attribute of our class, **_school**, should be **set and retrieved**. Indeed, we can now define a function called a **“setter”**, via **@school.setter**, which will be called whenever the school property is set. Here, we’ve made our setter validate values of school for us. Why _school and not school? **school is a property of our class**, with functions via which a user attempts to set our class attribute. **_school is that class attribute itself**. 

The **leading underscore, _,** indicates to users they need **not modify this value** directly. _school should only be set through the school setter. Notice how the school property simply returns that value of _school, our class attribute that has presumably been validated using our school setter. When a user calls student.school, they’re getting the value of _school through our school **“getter”**.

## Class Methods

Sometimes, we want to add functionality to a class itself, not to instances of that class. `@classmethod` is a function that we can use to add functionality to a class as a whole.

```Python 
import random

class Hat:

    schools = ["Stanford", "Oxxford", "Harvard", "UCLA"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.schools))


Hat.sort("Jack")
```

We don’t need to instantiate a hat anywhere in our code. `self`, therefore, is no longer relevant and is removed. We specify this sort as a `@classmethod`, replacing `self` with cls. Finally, notice how Hat is capitalized by convention near the end of this code, because this is the name of our class.

### Example 2

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
```

## Inheritance

We can create a class that “inherits” methods, variables, and attributes from another class. Within the “child” class Student, Student can inherit from the “parent” or “super” class Wizard as the line `super().__init__(name)` runs the init method of Wizard

```Python 
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")
```

## Operator Overloading

Some operators such as + and - can be “overloaded” such that they can have more abilities beyond simple arithmetic.

```Python 
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

total = potter + weasley
print(total)
```

The `__add__` method allows for the addition of the values of two vaults. `self` is what is on the left of the + operand. other is what is right of the +. This operator overloading is what some containers use to add their elements, such as the lists or strings.
