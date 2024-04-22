# Regular Expressions

Regular expressions or **“regexes”** will enable us to examine **patterns within our code**. Python has an existing library called `re` that has a number of built-in functions that can validate user inputs against patterns.

One of the most versatile functions within the library re is search. The search library follows the signature `re.search(pattern, string, flags=0)`. In the world of regular expressions there are certain symbols that allow us to identify patterns.

```
.   any character except a new line
*   0 or more repetitions
+   1 or more repetitions
?   0 or 1 repetition
{m} m repetitions
{m,n} m-n repetitions
```

In Python, **raw strings** are strings that don’t format special characters—instead, each character is taken at face-value. Imagine `\n`, for example, in a regular string, these two characters become one: a special newline character. In a raw string, however, \n is treated not as \n, the special character, but as a single \ and a single n. **Placing an r in front of a string** tells the Python interpreter to treat the string as a raw string, similar to how placing an f in front of a string tells the Python interpreter to treat the string as a format string.

## Special symbols 

We have more special symbols at our disposal in validation:

```
^   matches the start of the string
$   matches the end of the string or just before the newline
[]    set of characters
[^]   complementing the set
```

For example if we want to validate an email we can do the following:

```Python
import re

email = input("What's your email? ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
```

Notice that ^ means to match at the start of the string. All the way at the end of our expression, $ means to match at the end of the string. [a-zA-Z0-9_] tells the validation that characters must be between a and z, between A and Z, between 0 and 9 and potentially include an _ symbol. Testing the input, you’ll find that many potential user mistakes can be indicated.

Finally we have the following special characters:

```
\d    decimal digit
\D    not a decimal digit
\s    whitespace characters
\S    not a whitespace character
\w    word character, as well as numbers and the underscore
\W    not a word character

A|B     either A or B
(...)   a group
(?:...) non-capturing version
```

So we can improve our validation regex like:

```Python
import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w.+\.(com|edu|gov|net|org)$", email):
    print("Valid")
else:
    print("Invalid")
```