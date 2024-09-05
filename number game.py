import random

# options = ("rock", "paper", "scissors")
# player = None
# computer = random.choice(options)
# running = True

# while running:

#     while player not in options:
#         player = input("Enter a choice (rock, paper, scissors): ")

#     print(f"player:{player}")
#     print(f"Compute: {computer}")

#     if player == computer:
#         print("It's a tie!")

#     elif player == "rock" and computer == "scissors":
#         print("You win!")
#     elif player == "paper" and computer == "rock":
#         print("You win!")
#     elif player == "scissors" and computer == "paper":
#         print("You win!")

#     else:
#         print("You lose")
    
#     if not input("play again? (y/n):").lower() == "y":
#        playing = False

# print("Thanks for playing!")

# ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │", 
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │", 
        "└─────────┘"),
    3: ("┌─────────┐",
        "│   ●     │",
        "│     ●   │",
        "│       ● │", 
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │", 
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │", 
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │", 
        "└─────────┘")

}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

for die in range(num_of_dice):
    for line in dice_art.get(dice[die]):
        print(line)

for die in dice:
    total += die 
print(f"total: {total}")