## Assert

The assert function in Python is used to verify that a specified condition is true at a specific point in a program. If the given condition is false, then assert generates an exception of type AssertionError and the program stops. It is a way to make sure that certain conditions that are assumed to be true in the code actually are true during execution.

```python
x = 10
assert x == 10, "x is not 10"
```

`assert` should not be used to handle errors that are expected to occur during normal program execution; instead, try and except blocks should be used to handle exceptions appropriately.

## PyTest

`pytest` is a third-party library that allows you to unit test your program. That is, you can test your functions within your program.
It allows us to run our program directly through it, such that we can more easily view the results of our test conditions.

Example to test a `square` function from a `calculator`program

```python
from calculator import square


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0
```

We just have to run this program with `pytest` in the terminal; `pytest test_calculator.py`

## Organizing Test into Folders

Unit testing code using multiple tests is so common that you have the ability to run a whole folder of tests with a single command.
But `pytest` will not allow us to run tests as a folder simply with this file (or a whole set of files) alone without a special `__init__` file. Even leaving this `__init__.py` file empty, pytest is informed that the whole folder containing `__init__.py` has tests that can be run.

Now, typing pytest test in the terminal, we can run the entire test folder of code.