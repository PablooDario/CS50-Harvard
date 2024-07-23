def main():
    greeting = input("Greeting: ")
    amount = value(greeting)
    print(f'${amount}')

def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith("hello"):
        return 100
    elif greeting.startswith("h"):
        return 20
    else:
        return 0

if __name__ == "__main__":
    main()
