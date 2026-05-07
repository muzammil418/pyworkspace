from re import findall

def main():
    my_str = "cat dog cat bat dog cat"

    temp = findall("cat", my_str)

    print(temp)




if __name__ == "__main__":
    main()