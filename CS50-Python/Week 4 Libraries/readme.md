# Libraries
One of the reasons Python is so popular is that there are numerous powerful third-party libraries that add functionality. We call these third-party libraries, implemented as a folder, “packages”.

In Python, a module is a single file that contains definitions, functions, and statements, whereas a package is a collection of modules in directories that give structure and hierarchy to the modules.

PyPI is a repository or directory of all available third-party packages currently available. Python has a package manager called `pip` that allows you to install packages quickly onto your system.

## Sys

`sys` is a module that allows us to take arguments at the command line. `argv` is a function within the `sys` module that allows us to learn about what the user typed in at the command line. 

```python
import sys
print("hello, my name is", sys.argv[1])
```

The program is going to look at what the user typed in the command line after the name of the program. Currently, the name of the program is stored in the first position of the **arg** list. 

If you type python name.py David into the terminal window, you will see hello, my name is David. Notice that sys.argv[1] is where David is being stored. 

If the user does not type the arguments we want, we can have problems within the code, so we can handle this errors in many forms; for exampel using `try` and `except`or with `sys.exit`.

### Sys Exit 

`exit` is a built-in function of `sys` that allows us to exit the program if an error was introduced by the user, this function also accept an argument, which will be printed before leaving the program. We can rest assured now that the program will never execute the final line of code and trigger an error. 
```python
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])
```

Therefore, `sys.argv` provides a way by which users can introduce information from the command line. `sys.exit` provides a means by which the program can exit if an error arises.