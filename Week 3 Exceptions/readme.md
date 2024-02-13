# Exceptions

Exceptions are things that go wrong within our coding. Syntax errors are those that require you to double-check that you typed in your code correction. Runtime errors refer to those created by unexpected behavior within your code. For example, perhaps you intended for a user to input a number, but they input a character instead. Your program may throw an error because of this unexpected input from the user.

An effective strategy to fix this potential error would be to create “error handling” to ensure the user behaves as we intend.

## Try & Except 

In Python `try` and `except` are ways of testing out user input before something goes wrong. 

```python
try:
    x = int(input("What's x?"))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
```

For best practice, we should only try the fewest lines of code possible that we are concerned could fail. 

```python
try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
```

- The `try` block lets you test a block of code for errors.
- The `except` block lets you handle the error.
- The `else` block lets you execute code when there is no error.
- The `finally` block lets you execute code, regardless of the result of the **try** and **except** blocks.