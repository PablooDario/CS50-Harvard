# Implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all.

def main():
    time = convert(input("What time is it? "))
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    min = int(minutes)
    minutes = str(1/6 * min).replace('.', '').replace('0', '')
    return float(hours + '.' + minutes)

if __name__ == "__main__":
    main()