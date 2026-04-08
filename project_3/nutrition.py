def main():
    user_input = input("input: ").lower()
    fruits = {
    "apple": 130,
    "apricots": 30,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 20,
    "lime": 20,
    "nectarines": 60,
    "oranges": 80,
    "peaches": 60,
    "pears": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "tangerines": 50,
    "watermelon": 80
}
    if user_input in fruits:
        print(fruits[user_input])

main()