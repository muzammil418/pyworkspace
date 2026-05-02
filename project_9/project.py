import string
from itertools import product

def main():
    target = input("enter the password: ")

    guess, attempts = brute_force_crack(target)

    print(guess, attempts)


def brute_force_crack(target):
    chars = string.ascii_lowercase   
    chars += string.ascii_uppercase  
    chars += string.digits           
    chars += string.punctuation

    attempts = 0
    length = len(target)

    for i in range(1, length + 1):
        for j in product(chars, repeat=i):
            guess = "".join(j)
            attempts += 1

            if guess == target:
                return guess, attempts
            
    return None, attempts


if __name__ == "__main__":
    main()