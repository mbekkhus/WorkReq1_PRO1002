# ----------------------------------------
# 1. Greeting and Age Check
# ----------------------------------------
name = input("What's your name? ")
age = int(input("How old are you? "))

if age >= 18:
    print(f"Hello, {name}! You can come in.")
else:
    print(f"Hello, {name}! You are too young to come in.")

# ----------------------------------------
# 4. Fruit Basket
# ----------------------------------------
fruit_basket = {
    "apple": 8,
    "banana": 12,
    "orange": 7
}
fruit = input("Enter the name of a fruit: ").lower()

if fruit in fruit_basket:
    print(f"There are {fruit_basket[fruit]} {fruit}s in the basket.")
    for letter in fruit:
        print(letter)
else: 
    print("We don't have that fruit.")

# ----------------------------------------
# 6. Menu Selection
# ----------------------------------------
menu = {
    "coffee": 25,
    "tea": 20,
    "juice": 30
}
order = input("What would you like to order? ").lower()

if order in menu:
    print(f"The price of {order} is {menu[order]} kr.")
else:
    print("Item not found.")

print("Full menu:")
for item in menu:
    print(f"{item}: {menu[item]} kr")

# ----------------------------------------
# 9. Guessing Game
# ----------------------------------------
secret_number = 7
guesses = []

while True: 
    user_input = input("Guess the secret number (between 1 and 10): ")  

    try: 
        guess = int(user_input)
    except ValueError:
        print("Please enter a valid number.")
        continue

    guesses.append(guess)

    if guess == secret_number:
        print(f"Congratulations! You've guessed the secret number {secret_number} in {len(guesses)} attempts.")
        break
    else:
        print("Wrong guess. Try again.")

print("Your previous guesses were:", guesses)

# ----------------------------------------
# 10. Shopping List Manager
# ----------------------------------------
shopping_list = []

while True: 
    item = input("Enter an item to add to your shopping list (or type 'done' to finish): ")

    if item == "done":
        break
    else:
        shopping_list.append(item)

print("Your shopping list:", shopping_list)

if len(shopping_list) > 3:
    print("You have a lot of items on your shopping list!") 
else:
    print("Your shopping list is manageable.")
