# Implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed

coinsAccepted = [25, 10, 5]
due = 50

while due > 0:
    #Insert Coin
    coin = int(input("Insert coin: "))
    if coin in coinsAccepted:
        due -= coin
    if due > 0:
        print("Amount Due:", due)

print("Change Owed:", -due)