def main():
    text = input("input: ")
    vowels = "aeiouAEIOU"
    result = ""

    for char in text:                 
        is_vowel = False

        for v in vowels:   
                       
            if char == v:
                is_vowel = True
                break  

        if not is_vowel:
            result += char             

    print(result)
main()