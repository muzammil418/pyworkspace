def main():
    print("what is the answer of great question of life, the universe, and everything?")
    answer = input().lower().strip()
    if answer == 42 or "forty-two" or "forty two":
        print("true")
    else :
        print("false")

main()
