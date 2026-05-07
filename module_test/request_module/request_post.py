import requests

def main():
    mylist = {"name": "muzammil", "age": 17}
    response = requests.post("https://httpbin.org/post", data=mylist)

    print(response.text)





if __name__ == "__main__":
    main()