# ROCK PAPER SCISSORS


import random


robot_score = 0
user_score = 0

# Available choices
choose_list = ["R", "S", "P"]


while True:

    # Robot makes a random choice
    robot_choose = random.choice(choose_list)

    # Get user's choice
    user_choose = input("What is your choice? : ").upper()

    # Exit the game
    if user_choose.upper() == "FINISH":
        break

    # Validate user's input
    if user_choose not in ("R", "S", "P"):
        print("You should write (R, S, P)")
        continue

    # Check for a draw
    if user_choose == robot_choose:
        print("It's a draw!")
        continue

    # User loses
    if (
        (user_choose == "R" and robot_choose == "P")
        or (user_choose == "S" and robot_choose == "R")
        or (user_choose == "P" and robot_choose == "S")
    ):
        print("You lose!")
        robot_score += 1

    # User wins
    else:
        print("You win!")
        user_score += 1

    # Check the game score
    if user_score == 3:
        print("---------------------------")
        print("You win the game!")
        print(f"Your score: {user_score}")
        print(f"Robot score: {robot_score}")
        break

    if robot_score == 3:
        print("---------------------------")
        print("You lose the game!")
        print(f"Your score: {user_score}")
        print(f"Robot score: {robot_score}")
        break


# Thanks for checking out my project!
# Follow me on GitHub: github.com/nzmahdi
# If you like this project, consider giving it a star!
