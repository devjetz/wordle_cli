import random
import os

os.system("title Wordle_CLI")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

WORDS_FILE = os.path.join(BASE_DIR, "WORDS.txt")

with open(WORDS_FILE, "r") as f:
    WORDS = f.read().splitlines()

TRIES = 6
COLOURS = {
    "green":"\033[42;37m",
    "yellow": "\033[43;30m",
    "grey": "\033[100;37m",
    "red": "\033[41;37m",

    "escape": "\033[0m"
}

banner =f"""
Welcome to Wordle_CLI!

This is how you play:
- The computer generates a secret 5 letter word for you
- You start by giving a guess
- Your guess will be evaluated, and each character is given a colour
- These colours have different meanings, which are:
    - {COLOURS['red']}RED{COLOURS['escape']} means that the given word is too long. The red applies to every character, and the round counts.
    - {COLOURS['grey']}GREY{COLOURS['escape']} means that the character is not in the word.
    - {COLOURS['yellow']}YELLOW{COLOURS['escape']} means that the letter is in the selected word, but incorrectly placed.
    - {COLOURS['green']}GREEN{COLOURS['escape']} means that the character is in the word and correctly placed.

Good luck!
"""
want_to_be_playing = True
while want_to_be_playing:
    WORD = random.choice(WORDS)
    won = False
    history = []
    os.system("cls")
    print(banner)
    for round in range(0,TRIES,1):
        temp_word = f"{WORD}"
        guess = input(f"ROUND {round+1}: \n~> ").lower()
        os.system("cls")
        if len(guess) == len(WORD):
            evaluation = []
            for index,char in enumerate(guess):
                char_eval = "grey"
                if char == WORD[index]:
                    char_eval = "green"
                elif char in temp_word:
                    char_eval = "yellow"
                    temp_word = temp_word.replace(char,"",1)
                evaluation.append(char_eval)

            text = ""   
            for index,colour in enumerate(evaluation):
                text += COLOURS[colour] + guess[index] + COLOURS["escape"]

            history.append(text)
        else:
            history.append(COLOURS["red"]+guess+COLOURS["escape"])

        print(banner)
        for _guess in history:
            print(_guess)

        if guess == WORD:
            won = True
            break
            
    if won:
        print(f"\nCorrect! You guessed correctly in {round+1} tries!")
    else:
        print(f"\nBooo! You couldn't do it. The word was {WORD}!")

    choice = input("Do you want to play again? (y/n)\n~> ").lower()
    if "n" in choice:
        want_to_be_playing = False

#Coded in 44 minutes (so slow :sob:)