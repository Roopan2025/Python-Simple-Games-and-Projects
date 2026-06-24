weight = int(input("Enter your weight: "))
unit = input("Enter your unit killogram or pounds (K or L): ").upper()
if unit == "K":
    weight = weight * 2.205
    unit = "pounds"
    print(f"Your weight is {round(weight, 1)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "killogram"
    print(f"Your weight is {round(weight, 1)} {unit}")
else :
    print(f"{unit} is not a valid unit")


