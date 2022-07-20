############### Blackjack Project #####################

# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

from day11_blackjack_art import logo
import os
import random


def clear():
    os.system("cls")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_starting_hand():
    return [random.choice(cards), random.choice(cards)]


def draw_card():
    return random.choice(cards)


def has_blackjack(hand):
    return sum(hand) == 21


def get_score(hand):
    return sum(hand)


def start_game():
    player_hand = draw_starting_hand()
    computer_hand = draw_starting_hand()
    draw_more = True

    while True:

        if get_score(player_hand) > 21:
            print(
                f"You lose!\nFinal hand: {player_hand}, Score: {get_score(player_hand)}")
            break
        if get_score(computer_hand) > 21:
            print(
                f"You win! Opponent's final hand: {computer_hand}, Score: {get_score(computer_hand)}")
            break

        if has_blackjack(computer_hand):
            print(
                f"Blackjack! The opponent won with a final hand of {computer_hand}")
            break
        if has_blackjack(player_hand):
            print(f"Blackjack! You won with a final hand of {player_hand}")
            break

        print(f"Your hand: {player_hand}. Score: {get_score(player_hand)}")
        print(
            f"Opponent's hand: {computer_hand}. Score: {get_score(computer_hand)}")

        if draw_more:
            draw_more_prompt = input(
                "Type 'y' to get another card or 'n' to pass: ").lower()
            if draw_more_prompt != "y":
                draw_more = False
                continue

            player_card = draw_card()
            if player_card == 11 and get_score(player_hand) + 11 > 21:
                player_card = 1

            player_hand.append(player_card)
            print(
                f"You draw a {player_card}.\nYour current hand: {player_hand}. Score: {get_score(player_hand)}")

        else:
            if get_score(computer_hand) <= 16:
                computer_card = draw_card()
                if computer_card == 11 and get_score(computer_hand) + 11 > 21:
                    computer_card = 1

                computer_hand.append(computer_card)
                print(
                    f"Opponent draws a {computer_card}.\nOpponent's hand: {computer_hand}. Score: {get_score(computer_hand)}")
            else:
                player_score = get_score(player_hand)
                computer_score = get_score(computer_hand)
                if player_score > computer_score:
                    print("You win!")
                else:
                    print("You lose!")

                print(
                    f"Your final hand: {player_hand}\nYour score: {player_score}")
                print(
                    f"Opponent's hand: {computer_hand}\nOpponent's score: {computer_score}")
                break

    play_again = input("Would you like to play again? 'y' or 'n': ").lower()
    if play_again == 'y':
        start_game()
    else:
        print("Goodbye!")


def main():
    start_game()


main()
