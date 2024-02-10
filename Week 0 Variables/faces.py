# Implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂  and any :( converted to 🙁 

def convert(string):
    string = string.replace(":)", "🙂")
    string = string.replace(":(", "🙁")
    return string

def main():
    myString = input()
    print(convert(myString))

main()