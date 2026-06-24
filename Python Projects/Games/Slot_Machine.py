# python slot machine program

import random

def spin_row():
    row = ['🍓','🍉','✈️','💃','🎁']
    spin = [random.choice(row) for _ in range(3)]
    return spin

def print_row(row):
    print("***************")
    print(' | '.join(row))
    print("***************")

def payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🎁":
            return bet * 10
        elif row[0] == "💃":
            return bet * 8
        elif row[0] == '✈️':
            return bet * 5
        elif row[0] == '🍉':
            return bet * 3
        elif row[0] == '🍓':
            return bet * 2
    return 0

def main():
    balance = 100
    print("***************************")
    print("Welcome to Python Slot")
    print("Symbols : 🍓 🍉 ✈️ 💃 🎁")
    print("***************************")

    while True:
        bet = input("Enter the bet amount: ")

        if not bet.isdigit():
            print("Please enter a number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds!")
            continue
        elif bet <= 0:
            print("Please bet greater than 0!")
            continue
        else:
            balance -= bet
        print(f"current balance : ${balance}")

        row = spin_row()
        print("Spinning...\n")
        print_row(row)
        get_payout = payout(row,bet)

        if get_payout > 0:
            print(f"You Won ${get_payout}")
        else:
            print("You Lost ! Better luck next time!")

        balance += get_payout

        if balance ==0:
            print("You have no money!")
            break

        choice = input("Do you want to continue? (y/n): ").lower()

        if choice != "y":
            break

    print("Thanks for Playing")

if __name__ == "__main__":
    main()