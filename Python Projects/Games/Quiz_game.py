import time

questions = (("Who Won IPL 2026 Trophy ? "),
             ("Which Country Has Largest Population ?"),
             ("Who is the CM of Tamilnadu ?"),
             ("How many bones are in the human body ? "),
             ("How many legs have Spider ? "))

options = (("A.RCB","B.CSK","C.MI","D.GT"),
           ("A.USA","B.China","C.India","D.Japan"),
           ("A.Stalin","B.EPS","C.Joseph Vijay","D.Seeman"),
           ("A.290","B.206","C.190","D.200"),
           ("A.4","B.2","C.3","D.8"))

answers = ("A" , "C" , "C" , "B" , "D")

guesses = []
q_num = 0
score = 0

print("Welcome to the Quiz Game")
time.sleep(0.5)

name = input("Enter your name: ")
time.sleep(0.5)

for question in questions:
    print("--------------------------------")
    print(f"{q_num+1}. {question.upper()}")
    for option in options[q_num]:
        print(option.upper())
    guess = input("Select an option: ").upper()
    guesses.append(guess)
    if guesses[q_num] == answers[q_num]:
        print("Correct answer!")
        score += 1
    else:
        print(f"{answers[q_num]} is the correct answer!")
    q_num += 1
    time.sleep(0.5)

time.sleep(0.5)

print("---------------------------------")
print("              RESULT             ")
print("---------------------------------")

time.sleep(0.5)

print(f"Correct answers: ",end="")
for answer in answers:
    print(answer,end=" ")
print()

time.sleep(0.5)

print("Your guesses: ",end="")
for guess in guesses:
    print(guess,end=" ")
print()

time.sleep(0.5)

Total = (score / q_num) * 100
if Total >= 80:
    print(f"{name.capitalize()} you got {Total}% score")
    print("     Congratulations!     ")
else:
    print(f"{name.capitalize()} you got {Total}% score only")
    print("     Better Luck Next time!     ")

time.sleep(0.5)
print("Thanks for participating!")










