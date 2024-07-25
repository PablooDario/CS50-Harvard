import re

def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\b\W*um\b\W*"
    myUm = re.findall(pattern, s, re.IGNORECASE)
    return len(myUm)


if __name__ == "__main__":
    main()
