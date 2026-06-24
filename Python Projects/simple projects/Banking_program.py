# Simple Banking Program

def show_balance(balance):
    print("**************************************")
    print(f"Your current balance is ${balance:.2f}")

def deposit():
    print("**************************************")
    deposit_amount = float(input("Enter the deposit amount: "))
    
    if deposit_amount < 0 :
        print("**************************************")
        print("Please enter a valid deposit amount")
        return 0
    else:
        return deposit_amount

def withdraw(balance):
    print("**************************************")
    withdraw_amount = float(input("Enter the withdraw amount: "))

    if withdraw_amount > balance :
        print("**************************************")
        print("you cannot have sufficient balance")
        return 0
    elif withdraw_amount < 0 :
        print("**************************************")
        print("Please enter a valid withdraw amount")
        return 0
    else:
        return withdraw_amount

def bank():
    balance = 0
    is_running = True

    while is_running:
        print("**************************************")
        print("    Welcome to the Banking Program    ")
        print("***************************************")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("**************************************")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("**************************************")
            print("Please enter a valid choice")

    print("**************************************")
    print("Thank you ! have a nice day !")
    print("**************************************")

if __name__ == "__main__":
    bank()

