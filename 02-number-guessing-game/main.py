# Import randint to generate random numbers
from random import randint


# Generate the secret number that the player needs to guess
secret_number = randint(1, 50)

# The player starts with 3 lives
lives = 3

# This variable keeps track of whether the player has won
win = False


# -------------------- Game Start --------------------

print("--------------------")
print("Welcome to the Number Guessing Game!")
print("Guess the secret number between 1 and 50.")
print("--------------------")


# Keep asking the player to guess until they win or lose
while win == False:

    # Get the player's guess
    try:
        guess = int(input("Guess the number: "))

    except ValueError:
        print("Please enter a valid number!")
        print("--------------------")
        continue


    # Check if the guess is within the allowed range
    if guess < 1 or guess > 50:
        print("The number must be between 1 and 50!")
        print("--------------------")
        continue


    # Check if the player's guess is correct
    if guess == secret_number:
        win = True

        print("--------------------")
        print("WOW! You guessed the number!")
        print(f"You had {lives} lives left.")
        print("You WIN!")
        print("--------------------")

        break


    # Tell the player if their guess is too high
    elif guess > secret_number:
        print("The secret number is smaller!")


    # Tell the player if their guess is too low
    elif guess < secret_number:
        print("The secret number is bigger!")


    # Remove one life after an incorrect guess
    lives -= 1

    print(f"Lives remaining: {lives}")
    print("--------------------")


    # Check if the player has lost all their lives
    if lives == 0:

        print("You have no lives left!")
        print("--------------------")

        # Generate new numbers for the math challenge
        num1 = randint(0, 9)
        num2 = randint(0, 9)

        answer = input(
            "Do you want to earn an extra life? (yes / no): "
        ).lower()


        # Check if the player wants to continue
        if answer == "yes":

            print("--------------------")
            print("MATH CHALLENGE")
            print("--------------------")

            question = int(
                input(f"What is the result of {num1} * {num2}? ")
            )


            # Check if the math answer is correct
            if question == num1 * num2:

                lives += 2

                print("--------------------")
                print("Correct!")
                print("You gained an extra life!")
                print(f"Lives remaining: {lives}")
                print("--------------------")

                continue


            # The player failed the math challenge
            else:

                print("--------------------")
                print("Wrong answer!")
                print("The math challenge failed.")
                print("You LOST!")
                print("--------------------")

                break


        # The player does not want to continue
        else:

            print("--------------------")
            print("You chose not to continue.")
            print("You LOST!")
            print("--------------------")

            break
        
# Thanks for checking out my project!
# Follow me on GitHub: github.com/nzmahdi
# If you like this project, consider giving it a star!
# to be honest the AI design the print(-----) and writing the commands to make it clear!
