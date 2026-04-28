import validators

def main():
    email = input("what's your email: ")

    if validators.email(email):
        print("valid")

    else:
        print("invalid")



if __name__ == "__main__":
    main()