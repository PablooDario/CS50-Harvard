import random


def main():
    n = get_level()
    score = generate_integer(n)
    print(f"Score: {score}")

def get_level():
    levels = [1, 2, 3]
    while True:
        try:
            n = int(input("Level: "))
            if n in levels:
                return n
        except ValueError:
            pass


def generate_integer(level):
    grade = 10
    if level == 1:
        a, b = 0, 9
    elif level == 2:
        a, b = 10, 99
    else:
        a, b = 100, 999
    for _ in range(10):
        x, y = random.randint(a,b), random.randint(a,b)
        z = x + y
        error = 0
        while error != 3:
            try:
                user = int(input(f"{x} + {y} = "))
                if user == z:
                    break
                else:
                    print("EEE")
                    error += 1
            except ValueError:
                print("EEE")
                error += 1
        if error == 3:
            print(f"{x} + {y} = {z}")
            grade -= 1
    return grade

if __name__ == "__main__":
    main()