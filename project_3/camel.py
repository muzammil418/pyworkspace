def main():
    camel = input()
    snake = ""

    for i in range(len(camel)):
        ch = camel[i]

        if i == 0:
            snake += ch.lower()

        if ch.isupper():
            if i != 0:
                snake += "_"
                snake += ch.lower()
        else:
            snake += ch
    print(snake)

main()
