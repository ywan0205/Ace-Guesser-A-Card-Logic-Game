import sys
import random

# Define card value and suit rankings
VAL_RANK = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
            "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
SUIT_RANK = {"Clubs": 1, "Diamonds": 2, "Hearts": 3, "Spades": 4}

CARD_VALUES = list(VAL_RANK.keys())
CARD_SUITS = list(SUIT_RANK.keys())

def guessing_card(opponent_card: tuple[str, str], lowest_card: tuple[str, str], highest_card: tuple[str, str]) -> int:
    """
    Main card guessing function, allows up to 10 attempts and returns a score based on performance.
    """
    max_attempts = 10  # Maximum number of attempts
    attempts = 0       # Current attempt count

    while attempts < max_attempts:
        # Prompt the player to guess within the current card range
        guess_input = input(f"Guess the card [({lowest_card[0]},{lowest_card[1]}) ~ ({highest_card[0]},{highest_card[1]})]: ")
        try:
            guess_value, guess_suit = map(str.strip, guess_input.split(','))
        except ValueError:
            print("Invalid format! Please enter like: 7,Spades\n")
            continue

        guess_value = guess_value.capitalize()
        guess_suit = guess_suit.capitalize()

        # Validate the input
        if guess_value not in VAL_RANK or guess_suit not in SUIT_RANK:
            print("Invalid card value or suit! Try again.\n")
            continue

        # If the guess is correct
        if (guess_value, guess_suit) == opponent_card:
            print(f"\nCorrect! You found the card in {attempts+1} attempts!")
            score = max(0, 100 - attempts * 10)  # 每错一次扣 10 分
            print(f"Your score: {score}\n")
                        # Add performance evaluation
            if score == 100:
                print("Excellent! 🌟")
            elif score >= 70:
                print("Great job! 👍")
            elif score >= 40:
                print("Not bad, keep practicing! 💡")
            else:
                print("Better luck next time! 🎲")
            return score

        # Determine if the guess is too high or too low, and provide detailed feedback
        if VAL_RANK[guess_value] > VAL_RANK[opponent_card[0]]:
            if SUIT_RANK[guess_suit] > SUIT_RANK[opponent_card[1]]:
                print("Your guess is too high in value. 📈")
                print("Your guess is too high in suit. 📈")
            elif SUIT_RANK[guess_suit] < SUIT_RANK[opponent_card[1]]:
                print("Your guess is too high in value. 📈")
                print("Your guess is too low in suit. 📉")
            else:
                print("Your guess is too high in value. 📈")
                print("Your suit is correct! ✔️")
            print("That guess was incorrect. (-10 points)\n")
            highest_card = (guess_value, guess_suit)
        elif VAL_RANK[guess_value] < VAL_RANK[opponent_card[0]]:
            if SUIT_RANK[guess_suit] > SUIT_RANK[opponent_card[1]]:
                print("Your guess is too low in value. 📉")
                print("Your guess is too high in suit. 📈")
            elif SUIT_RANK[guess_suit] < SUIT_RANK[opponent_card[1]]:
                print("Your guess is too low in value. 📉")
                print("Your guess is too low in suit. 📉")
            else:
                print("Your guess is too low in value. 📉")
                print("Your suit is correct! ✔️")
            print("That guess was incorrect. (-10 points)\n")
            lowest_card = (guess_value, guess_suit)
        else:
            # Value is correct, compare suits
            print("You got the value correct! Keep it up! 🎯")
            if SUIT_RANK[guess_suit] > SUIT_RANK[opponent_card[1]]:
                print("But your suit is too high. Don’t give up! 🔼")
                print("That guess was incorrect. (-10 points)\n")
                highest_card = (guess_value, guess_suit)
            elif SUIT_RANK[guess_suit] < SUIT_RANK[opponent_card[1]]:
                print("But your suit is too low. You're close! 🔽")
                print("That guess was incorrect. (-10 points)\n")
                lowest_card = (guess_value, guess_suit)
            else:
                print("And you also got the suit correct! Amazing! 🎉")

        attempts += 1
        remaining = max_attempts - attempts
        print(f"Attempts remaining: {remaining}")
        current_score = max(0, 100 - attempts * 10)
        print(f"Current score: {current_score}\n")

    # Ran out of attempts without a correct guess
    print(f"\nOut of attempts! The correct card was: {opponent_card[0]}, {opponent_card[1]}\n")
    print("Better luck next time! 🎲")
    return 0


def main():
    # Welcome message
    print("Welcome to Card Guessing Game Plus!\n")
    print("Available card values (in order): 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace")
    print("Available suits (in order): Clubs, Diamonds, Hearts, Spades\n")

    while True:
        # System randomly selects the target card
        value = random.choice(CARD_VALUES)
        suit = random.choice(CARD_SUITS)
        opponent_card = (value, suit)
        print("A secret card has been randomly selected. Try to guess it!")

        # Initialize guessing range
        lowest_card = ("2", "Clubs")
        highest_card = ("Ace", "Spades")

        # Start the guessing round
        guessing_card(opponent_card, lowest_card, highest_card)

        # Ask the player if they want to play again
        again = input("Play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("\nThanks for playing! Goodbye~")
            break

if __name__ == '__main__':
    main()
