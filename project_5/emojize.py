import emoji

def main():
    user_input = input("input: ")

    result = emoji.emojize(user_input, language="alias")

    print(f"output: {result}")


main()