import re

def main():
    my_str = "cat dog cat bat dog cat"

    match = re.finditer("cat", my_str)

    for i in match:
        print(i.group(), i.start(), i.end())




if __name__ == "__main__":
    main()