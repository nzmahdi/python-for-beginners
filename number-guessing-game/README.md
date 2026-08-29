# Number Guessing Game

A simple Number Guessing Game written in Python.

---

## Goal

The goal of this exercise is to practice Python basics by building an interactive number guessing game.

The player needs to guess a randomly generated secret number while managing a limited number of lives.

This project also includes a small math challenge that allows the player to earn extra lives after running out of lives.

---

## What I Learned

While building this project, I practiced and learned:

- Using variables to store data
- Getting user input with `input()`
- Converting input using `int()`
- Using `if`, `elif`, and `else` statements
- Using `while` loops
- Using `break` and `continue`
- Using the `random` module
- Generating random numbers with `randint()`
- Comparing values with conditional operators
- Using `try` and `except` for error handling
- Handling invalid user input with `ValueError`
- Keeping track of lives using variables
- Creating game logic with conditions
- Building a simple math challenge
- Working with user choices using `.lower()`

---

## How to Play

The game generates a secret number between **1 and 50**.

You have **3 lives** to guess the secret number.

After each incorrect guess, the game tells you whether the secret number is:

- **Smaller** than your guess
- **Bigger** than your guess

If you guess the number correctly, you win the game.

---

## Extra Life Challenge

If you lose all your lives, you have the option to continue by completing a math challenge.

The game generates two random numbers and asks you to calculate their multiplication.

If your answer is correct:

- You gain **2 extra lives**
- You can continue guessing

If your answer is wrong, you lose the game.

---

## Rules

- The secret number is between `1` and `50`.
- You start with **3 lives**.
- Each incorrect guess costs **1 life**.
- You cannot enter a number outside the range `1-50`.
- Invalid inputs are handled by the program.
- If you run out of lives, you can try the math challenge.
- A correct math answer gives you **2 extra lives**.
- Guess the secret number to win.

---

## Exit the Game

The game does not have a specific exit command.

The game ends when:

- You guess the secret number.
- You lose all your lives and fail the math challenge.
- You choose not to continue after losing all your lives.

---

## Requirements

- Python 3.x
- No external libraries required

This project only uses Python's built-in `random` module.

---

## Run the Game

Open a terminal in the project folder and run:

```bash
python main.py
```
---

## Author 
Created by **nzmahdi**
[GitHub Profile⁠](https://github.com/nzmahdi)
If you like this project, consider giving it a **star**!
