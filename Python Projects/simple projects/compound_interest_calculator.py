principle = 0
interest_rate= 0
time = 0

while principle <=  0:
    principle = float(input("Enter a principle: "))
    if principle <= 0:
        print("principle cannot be less than or equal to zero.")

while True:
    interest_rate = float(input("Enter a interest_rate: "))
    if interest_rate <= 0:
        print("interest_rate cannot be less than or equal to zero.")
    else:
        break

while time <=  0:
    time = int(input("Enter a time in years: "))
    if time <= 0:
        print("time cannot be less than or equal to zero.")

total = principle * pow(( 1 + interest_rate/100 ),time)
print(f"balance after {time} years : ${total:,.2f}")