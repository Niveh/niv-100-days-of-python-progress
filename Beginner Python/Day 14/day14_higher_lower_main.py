import os
import random
from day14_higher_lower_art import logo, vs
from day14_higher_lower_data import data


def clear():
    os.system("cls")


def get_random_celebs():
    celeb_one = random.choice(data)
    celeb_two = random.choice(data)

    while celeb_one == celeb_two:
        celeb_two = random.choice(data)

    return (celeb_one, celeb_two)


def run_game_intro(score=0):
    clear()
    print(logo)
    start_game(score)


def start_game(score=0):
    celeb_a, celeb_b = get_random_celebs()

    print(
        f'Compare A: {celeb_a["name"]}, a {celeb_a["description"]}, from {celeb_a["country"]}.')
    print(vs)
    print(
        f'Against B: {celeb_b["name"]}, a {celeb_b["description"]}, from {celeb_b["country"]}')

    guess = input("Who has more followers? Type 'A' or 'B': ").strip().lower()
    while guess not in "a b":
        guess = input(
            "Invalid input!\nWho has more followers? Type 'A' or 'B': ").strip().lower()

    answer = "a" if celeb_a["follower_count"] > celeb_b["follower_count"] else "b"

    clear()
    print(logo)
    if guess == answer:
        score += 1
        print(f"You've guessed correctly! Current Score: {score}")
    else:
        print(f"Sorry, that's wrong. Current Score: {score}")

    print(f'{celeb_a["name"]} has {celeb_a["follower_count"]}M followers.')
    print(f'{celeb_b["name"]} has {celeb_b["follower_count"]}M followers.')

    play_again = True if input(
        "Type 'yes' to play again, anything else to exit: ").strip().lower() == 'yes' else False

    if play_again:
        run_game_intro(score)
    else:
        print("Goodbye!")


def main():
    run_game_intro()


main()
