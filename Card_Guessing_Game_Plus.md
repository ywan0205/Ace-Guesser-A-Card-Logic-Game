
# 🃏 Card Guessing Game Plus

**Card Guessing Game Plus** is a Python-based logic and guessing game where the player tries to identify a secret playing card randomly selected by the computer. The game is designed to help practice conditional logic, user input handling, and score-based feedback.

---

## 🎮 How to Play

1. The system randomly chooses a card from a standard 52-card deck (value + suit).
2. You have **10 attempts** to guess the correct card.
3. Input your guess in the format: `Value,Suit`  
   Example: `10,Hearts` or `Queen,Spades`
4. After each guess, you'll receive detailed feedback:
   - Whether the value is too high, too low, or correct.
   - Whether the suit is too high, too low, or correct.
5. You earn up to **100 points**, with **-10 points** per wrong guess.
6. After each guess, remaining attempts and current score will be shown.
7. At the end of the game, you'll receive a performance evaluation (e.g., Excellent, Great Job, etc.)

---

## 🧠 Concepts Demonstrated

- Random card selection using `random.choice`
- String parsing and input validation
- Conditional logic and ranking comparison
- Score calculation and feedback
- Looping with attempt limits
- Friendly UI using emojis and messages

---

## ▶️ Running the Game

To play, run the script with:

```bash
python card_guessing_game.py
```

Ensure you have Python 3 installed. No external libraries are required.

---

## 🗂️ File Structure

- `card_guessing_game.py` – main game logic

---

## ✨ Sample Output

```
Welcome to Card Guessing Game Plus!

Available card values (in order): 2, 3, ..., King, Ace
Available suits (in order): Clubs, Diamonds, Hearts, Spades

A secret card has been randomly selected. Try to guess it!
Guess the card [(2,Clubs) ~ (Ace,Spades)]: Queen,Hearts
Your guess is too high in value.
Your guess is too high in suit.
That guess was incorrect. (-10 points)

Attempts remaining: 9
Current score: 90
```

---

Enjoy the challenge, and may you find the Ace! ♠️
