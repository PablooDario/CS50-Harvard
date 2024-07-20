# Implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

def main():
    quant = fuel()
    if quant <= 1:
        print('E')
    elif quant >= 99:
        print('F')
    else:
        print(f"{quant}%")

def fuel():
    #prompt the user for a fraction
    while True:
        quantity = input("Fraction: ")
        idx = quantity.find('/')

        # check if x and y are integers
        try:
            x = int(quantity[:idx])
            y = int(quantity[idx+1:])
            if x > y :
                continue
        except ValueError:
            continue

        # y is 0
        try:
            quantity = round((x/y) * 100)
            return quantity
        except ZeroDivisionError:
            pass

main()