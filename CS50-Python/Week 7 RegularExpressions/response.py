import validators

def main():
    user_email = input("Enter your email: ")
    if validators.email(user_email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()