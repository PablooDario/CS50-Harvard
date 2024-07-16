# Implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z

exp = input("Expression: ")
exp = exp.strip()
x, y, z = exp.split(" ")
x = int(x)
z = int(z)
if y == '+':
    print(float(x + z))
elif y == '-':
    print(float(x - z))
elif y == '*':
    print(float(x * z))
else:
    print(x / z)