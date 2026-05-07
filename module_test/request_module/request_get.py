import requests

def main():
    response = requests.get("https://chatgpt.com")
    print(response.text)




if __name__ == "__main__":
    main()