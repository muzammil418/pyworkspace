def main():
    text = input("input: ")
    print(shorten(text))


def shorten(word):
    vowels = "aeiouAEIOU"
    result = ""

    for char in word:
        is_vowel = False

        for v in vowels:
            if char == v:
                is_vowel = True
                break

        if not is_vowel:
            result += char

    return result


if __name__ == "__main__":
    main()