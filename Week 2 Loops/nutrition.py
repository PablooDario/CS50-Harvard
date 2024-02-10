# Implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit

def main ():
    fruit = input("Item: ").title()
    print(calories(fruit), end="")

def calories(fruit):

    nutritionFacts = {
        "Apple" : 130,
        "Avocado" : 50,
        "Banana" : 110,
        "Cantaloupe" : 50,
        "Grapefruit" : 60,
        "Grapes" : 90,
        "Honeydew Melon" : 50,
        "Kiwifruit" : 90,
        "Lemon" : 15,
        "Lime" : 20,
        "Nectarine" : 60,
        "Orange" : 80,
        "Peach" : 60,
        "Pear" : 100,
        "Sweet Cherries" : 100
    }

    if fruit not in nutritionFacts:
        return ""
    return nutritionFacts[fruit]

main()