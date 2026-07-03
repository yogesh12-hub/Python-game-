
import random

print("Welcome To The Game Rock Paper Scissor")

option = ["Rock", "Paper", "Scissor"]

while True:

    print("\nYour Choices:", option)
    uin = input("Enter Your Choice: ")
    uin = uin.capitalize()

    if uin not in option:
        print("Invalid Input")
        continue

    comp = random.choice(option)

    print(f"You chose: {uin}")
    print(f"Computer chose: {comp}")

    # Tie
    if comp == uin:
        print("Game is Tie")

    # Computer Wins
    elif (comp == "Rock" and uin == "Scissor") or \
         (comp == "Paper" and uin == "Rock") or \
         (comp == "Scissor" and uin == "Paper"):
        print("Computer Wins")

    # User Wins
    else:
        print("You Win")

    # Play Again
    play = input("\nDo you want to play again? (Y/N): ")

    if play.lower() != "y":
        print("Thank You For Playing!")
        break
