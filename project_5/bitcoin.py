import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
        if n <= 0:
            sys.exit("Number must be positive")
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        response = requests.get(url)
        data = response.json()

        price = float(data["bpi"]["USD"]["rate"].replace(",", ""))

    except requests.RequestException:
        sys.exit("API request failed")

    total = n * price

    print(f"${total:,.4f}")


if __name__ == "__main__":
    main()