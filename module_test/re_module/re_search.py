import re 

def main():
    my_str = "i have a cat and a dog"

    if re.search("cat", my_str):
        print("find")
    else:
        print("not found")




if __name__ == "__main__":
    main()