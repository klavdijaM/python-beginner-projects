import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

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
guessed_letters = [] #[l
lives = 6

# keep guessing until won
while not hasWon and lives>0:
    guess = input("Guess a letter: ").lower() #l
    guessed_letters.append(guess)

    # displaying correctly guessed letters
    display = ""
    correct_guess = False
    for letter in chosen_word: #lantern - la
        if letter in guessed_letters:
            display += letter #l
            if letter == guess: # revise later
                correct_guess = True
        else:
            display += "_"
    print(display)

    if correct_guess:
        print("Nice, keep going!")
    else:
        # losing lives for wrong guesses
        if guess not in chosen_word:
            lives -= 1
            print(stages[lives])
            print(f"Oops, wrong guess! You have {lives} lives left")

    if "_" not in display:
        hasWon = True
        print("Congratulations! You saved the stickman! 🥳")

if lives == 0 and not hasWon:
    print("You ran out of lives. RIP stickman 💀")




