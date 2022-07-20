# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import os
from day12_number_guessing_art import logo

GAME_MODES = ["easy", "hard"]


def clear():
    os.system("cls")


def run_game_intro():
    clear()
    print(logo)
    print("Welcome to the number guessing game!")
    print("Your goal is to guess the number between 1 and 100.")
    print("Available Game Modes:\nEasy (10 lives)\nHard (5 lives)")
    mode = get_game_difficulty()

    if mode in GAME_MODES:
        start_game(mode)
    else:
        print("Invalid game mode!\nExiting...")


def get_game_difficulty():
    diff = input(
        "Type 'easy' for Easy mode or 'hard' for Hard mode: ").strip().lower()
    if diff not in GAME_MODES:
        return "invalid"
    return diff


def get_guess_count(lives, mode):
    if mode == "easy":
        return 10 - lives
    if mode == "hard":
        return 5 - lives


def start_game(mode):
    clear()
    number = random.randint(1, 100)
    lives = 0

    if mode == "easy":
        lives = 10
    elif mode == "hard":
        lives = 5
    print(f"Game starting in {mode} mode!")

    while lives > 0:
        guess = int(input("Enter your guess (1-100): "))
        if guess == number:
            print(
                f"You've guessed correctly!\nThe number was {number}, guessed after {get_guess_count(lives, mode) + 1} tries.")
            break
        elif guess > number:
            print(f"Too high! {lives - 1} guesses left.")
        elif guess < number:
            print(f"Too low! {lives - 1} guesses left.")
        lives -= 1

    if lives == 0:
        print(
            f"You ran out of guesses! The number was {number}.")

    play_again = True if input(
        "Type 'yes' to play again, anything else to exit: ").strip().lower() == 'yes' else False

    if play_again:
        run_game_intro()


def main():
    run_game_intro()


main()
