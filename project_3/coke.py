def main():
    print("Price 50 cents")
    price = 50


    while True:
        coin = int(input("insert the coin: "))

        if coin in [5, 10, 25]:
            price -= coin
            if price > 0:
                print(f"Amount due: {price} cents")
            else:
                break

        else:
            continue

    print(f"Change owed: {abs(price)} cents")

main()