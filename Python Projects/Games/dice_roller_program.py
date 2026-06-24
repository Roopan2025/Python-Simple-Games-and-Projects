import random
#
# # print(" \u25cf \u250c \u2500 \u2510 \u2502 \u2514 \u2518")
#
# # ● ┌ ─ ┐ │ └ ┘
#
# # "┌─────────┐"
# # "│         │"
# # "│         │"
# # "│         │"
# # "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"),
}


dices = []
total = 0
rolls = int(input("How many dice do you want? "))

for dice in range(rolls):
    num = random.randint(1,6)
    dices.append(num)
# print(dices)

# for dice in range(rolls):                  # for row wise printing
#     for art in dice_art.get(dices[dice]):
#         print(art)

for dice in range(5):                         # for horizontal printing
    for col in dices:
        art = dice_art.get(col)
        print(art[dice], end=" ")
        # print(dice_art.get(col)[dice],end=" ")

    print()

for dice in dices:
    # print(dice)
    total = total + dice
print(f"Total : {total}")




# for understanding

# a= {
#     1: ("123","123","123"),
#     2: ("234","234","234"),
#     3: ("345","345","345"),
#     4: ("456","456","456"),
# }
# b=int(input("How many dice do you want? "))
# c=[]
#
# for i in range(b):
#     c.append(random.randint(1,4))
# print(c)

# for x in range(b) :             # for vertical printing
#     for y in a.get(c[x]):
#         print(y)

# for x in range(3):                # for horizontal printing
#     for y in c:
#         d = a.get(y)
#         print(d[x], end=" ")
#     print()











