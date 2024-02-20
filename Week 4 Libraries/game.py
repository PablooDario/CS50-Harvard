import random

n = 0
while n < 1:
    try:
        n = int(input("Level: "))
    except ValueError:
        pass

level = random.randint(1, n)

while True:
    try:
        n = int(input("Guess: "))
        if n > 0:
            if n < level:
                print("Too small!")
            elif n > level:
                print("Too large!")
            else:
                print("Just right!")
                break 
    except ValueError:
        pass
    else:
        if n < 1:
            pass
        