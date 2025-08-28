import random

word_list = ["lantern", "harbor", "meadow", "whisper", "metamorphosis", "perpendicularity"]

chosen_word = random.choice(word_list)
print(chosen_word)

# displaying a placeholder for all letters in the chosen word
placeholder = ""
for letter in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

# game start
print("Welcome to Hangman! - A game where your spelling skills can save lives (or end them 👀)")
print("Good Luck!")
hasWon = False
guessed_letters = []

# keep guessing until won
while not hasWon:
    guess = input("Guess a letter: ").lower() #l
    guessed_letters.append(guess) #l

    # displaying correctly guessed letters
    display = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        hasWon = True
        print("Congratulations! You saved the stickman! 🥳")




