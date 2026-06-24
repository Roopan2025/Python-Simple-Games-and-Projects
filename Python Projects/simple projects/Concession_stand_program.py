menu = {"pizza": 3.00,
        "chicken": 2.00,
        "popcorn": 6.00,
        "chips": 1.5,
        "fries":2.2,
        "soda":1.2}

cart = []
total = 0

print("------- Menu -------")
for key, value in menu.items():
    print(f"{key:10}:  ${value:.2f}")

while True:
    food = input("Enter your orders ( q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print(f"{food} is not available")

print("------------------------")
print("       Your Orders      ")
print("------------------------")

for food in cart:
    total += menu.get(food)
    print(f"{food :10} :  ${menu.get(food):.2f} ")
print("------------------------")
print(f"Total      :  ${total:.2f}")











