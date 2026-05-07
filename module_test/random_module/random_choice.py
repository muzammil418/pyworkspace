import random

def main():
    mylist = []
    print("enter number: ", end="")

    for i in range(5):
        temp = input()
        temp = int(temp)
        mylist.append(temp)

    temp = random.choice(mylist)

    print(f"random number {temp}")




if __name__ == "__main__":
    main()