
Foods = []
Prices = []
Total = 0

while True:
    food = input("Enter food you want to buy (q to quit): ")
    if food.lower() == "q":
        break
    else :
        price = float(input("Enter price for your food : $ "))
        Foods.append(food)
        Prices.append(price)
print("----- YOUR CART -----")
for food in Foods:
     print(f"{food.upper()} --- ${Prices[Foods.index(food)]}")
for price in Prices:
    Total = Total + price
print(f"TOTAL --- ${Total}")