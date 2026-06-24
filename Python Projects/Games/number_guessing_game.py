import random

low_num = 1
high_num = 100
answer = random.randint(low_num, high_num)
guesses = 0
is_running = True

print("Welcome to Number Guessing Game")
print(f"find the number between {low_num} and {high_num}")

while is_running:

    num = input("Guess the number: ")  # get the number as a string

    if num.isdigit():                  # isdigit method return True or False # check the string is a digit
        num = int(num)                 # perform Typecast(convert string into integer)
        guesses += 1

        if num < low_num or num > high_num:
            print("out of range")
            print(f"please select the number between {low_num} and {high_num}")

        elif num < answer:
            print("Your guess is too low")
            print("guess higher!")

        elif num > answer :
            print("Your guess is too high")
            print("guess lower!")

        else:
            print("you guessed correctly")
            print(f"The number is {answer}")
            print(f"you use {guesses} guesses to find the number")
            play_again = input("you want to play again?( Y or N ) ").lower()

            if play_again == "y":
                is_running = True
                print("Welcome to Number Guessing Game")
                print(f"find the number between {low_num} and {high_num}")

            elif play_again == "n":
                print("Thank you for playing")
                is_running = False

            else:
                while True :

                    play_again=input("please enter Y or N : ").lower()

                    if play_again == "y":
                        is_running = True
                        print("Welcome to Number Guessing Game")
                        print(f"find the number between {low_num} and {high_num}")
                        break

                    elif play_again == "n":
                        is_running = False
                        print("Thank you for playing")
                        break

    else:
        print("invalid number")
        print(f"please select the number between {low_num} and {high_num}")



