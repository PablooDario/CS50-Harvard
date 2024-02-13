# Implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d. 
# After each inputted item, display the total cost of all items inputted thus far.

def main():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    order(menu)

def order(menu):
    total = float(0)
    while True:
        try:
            item = input("Item: ").title()
        except EOFError:
            print()
            return 
        try:
            total += menu[item]
            print(f"${total:.2f}")
        except KeyError:
            continue

main()