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
## Raw Strings

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

# If we found the pattern in the string
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

## Built-in flags

- **re.IGNORECASE** Makes the pattern non case sentitive
- **re.MULTILINE** Allows us to read or search in paragraphs instead of a single line
- **re.DOTALL** Allows the dot sign to search any character or especial character like '\n'

### Example

If we are looking to validate a bunch of emails that are in a txt or paragraph and and we don't care whether they are in upper or lower case letters, we can do the following:

```Python
import re

with open("emails.txt", "r") as file:
    emails = file.readlines()

pattern = r"^\w+@(\w+\.)?\w+\.edu$"

if re.search(pattern, emails, re.IGNORECASE, re.MULTILINE):
    print("Valid")
else:
    print("Invalid")
```

## Groups

`re.search` can return a set of matches that are extracted from the user’s input. We can request specific groups back using `matches.group`

If we want to extract the user of a twitter url we can do the following:

```Python
import re

url = input("URL: ").strip()
pattern = r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)"

if matches := re.search(pattern, url, re.IGNORECASE):
    print(f"Username:", matches.group(1))
```

First we are grouping the *www.* but we don´t want to store it, so we write `(?:www\.)`, then we group the username and we want to store it so we do the fllowing`([a-z0-9_]+)` 

## Substitute

Within the re library, there is a method called sub. This method allows us to substitute a pattern with something else. Notice how pattern refers to the regular expression we are looking for. Then, there is a repl string that we can replace the pattern with. Finally, there is the string that we want to do the substitution on.

`re.sub(pattern, repl, string, count=0, flags=0)`