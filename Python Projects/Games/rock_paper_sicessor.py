import random

options = ('rock','paper','scissors')
running = True

while running :

    player = None
    computer = random.choice(options)

    while player not in options:

        player = input("choose rock, paper or scissors: ")

    print(f"player chose: {player}")
    print(f"bot chose: {computer}")

    if player == computer:
        print("Draw")

    elif player == 'rock' and computer == 'scissors':
        print("You win!")

    elif player == 'paper' and computer == 'rock':
        print("You win!")

    elif player == 'sicessors' and computer == 'paper':
        print("You win!")

    else:
        print("You lose!")
        # play_again = input("play again? (y/n): ").lower()
        # if not play_again == 'y':
        #     running = False
        if not input('play again? (y/n): ').lower() == 'y':
            running = False


print("Thank you for playing")




