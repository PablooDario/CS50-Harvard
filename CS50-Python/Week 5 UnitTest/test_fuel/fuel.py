def main():
    quantity = input("Fraction: ")
    quant = convert(quantity)
    print(gauge(quant))


def convert(fraction):
    idx = fraction.find('/')
    # x or y is not an integer
    try:
        x = int(fraction[:idx])
        y = int(fraction[idx+1:])
        assert (x <= y) == True
    except (ValueError, AssertionError):
        raise ValueError
    # y is 0
    try:
        fraction = round((x/y) * 100)
        return fraction
    except ZeroDivisionError:
        raise ZeroDivisionError

def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()