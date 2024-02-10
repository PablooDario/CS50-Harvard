# Implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    n = len(s)
    digits = "2"

    # Special characters or invalid size
    if not s.isalnum() or (6 < n or n < 2):
        return False

    # First digit 0 or digits in the first 2 positions
    for i in range(n):
        if s[i].isdigit():
            if i < 2 or s[i] == '0':
                return False
            digits = s[i:]
            break

    if digits.isdigit():
        return True

    # Digits in the middle
    return False


main()