# Implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

vowels = ['a', 'e', 'i', 'o', 'u']
user = input("Input: ")

for u in user:
    if u.lower() in vowels:
        user = user.replace(u, '')

print("Output:", user)