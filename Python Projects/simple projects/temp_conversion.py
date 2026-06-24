temp = float(input("Enter your temperature: "))
unit = input("Is this temperature is celsius or fahrenheit? ( C or F ): ").upper()

if unit == "C":
    temp_new = round((temp * (9/5)) + 32,1)
    unit_new = "F"
    print(f"{temp}{unit} is the {temp_new}{unit_new}")
elif unit == "F":
    temp_new = round((temp - 32) * 5/9,1)
    unit_new = "C"
    print(f"{temp}{unit} is the {temp_new}{unit_new}")
else :
    print(f"{unit} is a invalid unit")