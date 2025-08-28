import random

word_list = ["lantern", "harbor", "meadow", "whisper", "metamorphosis", "perpendicularity"]

chosen_word = random.choice(word_list)
print(chosen_word)

# displaying a placeholder for all letters in the chosen word
placeholder = ""
for underscore in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

print("Welcome to Hangman! - A game where your spelling skills can save lives (or end them 👀)")
print("Good Luck!")
guess = input("Guess a letter: ").lower()

# displaying correctly guessed letters
display = ""
for letter in chosen_word: # wh
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)

