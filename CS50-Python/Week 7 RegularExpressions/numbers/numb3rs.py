import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Create search pattern
    pattern = r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$"
    # If we found the pattern in the string we will validate the IP address
    if res := re.search(pattern, ip):
        #Validate each number
        for group in res.groups():
            # If the byte is greater than 255 is false (We dont have to worry for negative values since we have the pattern)
            if int(group) > 255:
                return False
        return True
    #If we didn't found the pattern
    return False


if __name__ == "__main__":
    main()
