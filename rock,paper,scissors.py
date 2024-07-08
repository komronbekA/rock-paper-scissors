import random

options = ("rock", "paper", "scisors")
playing = True

while playing:
    player = None
    compyuter = random.choice(options)


    while player not in options:
        player = input("enter a choice (rock, paper scisors): ")

    print(f"player: {player}")
    print(f"Computer: {compyuter}")

    if player == compyuter:
        print("It's a tie!")

    elif player == "rock" and compyuter == "scissors":
        print("Player wins!")
    elif player == "paper" and compyuter == "rock":
        print("Player wins!")
    elif player == "scisors" and compyuter == "paper":
        print("Player wins!")
    else:
        print("Computer wins!")

    if not input("Play again? (y/n): ").lower() == "y":
        playing = False

print("thenls for playing!")


      