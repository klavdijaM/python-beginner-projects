import random

stages = [r'''
   +------+
   |      |
   O      |
  /|\     |
  / \     |
          |
===============
''', r'''
   +------+
   |      |
   O      |
  /|\     |
  /       |
          |
===============
''', r'''
   +------+
   |      |
   O      |
  /|\     |
          |
          |
===============
''', r'''
   +------+
   |      |
   O      |
  /|      |
          |
          |
===============
''', r'''
   +------+
   |      |
   O      |
   |      |
          |
          |
===============
''', r'''
   +------+
   |      |
   O      |
          |
          |
          |
===============
''', r'''
   +------+
   |      |
          |
          |
          |
          |
===============
''']

welcome_art = r'''
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝

████████╗ ██████╗
╚══██╔══╝██╔═══██╗
   ██║   ██║   ██║
   ██║   ██║   ██║
   ██║   ╚██████╔╝
   ╚═╝    ╚═════╝

██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
'''

word_list = ["lantern", "harbor", "meadow", "whisper", "ocean", "river"]

def display_board(lives, display):
    print(stages[lives])
    print("Word to guess:", " ".join(display))

def process_guess(chosen_word, guess, display):
    correct_guess = False

    for index, letter in enumerate(chosen_word): # iterates through each letter and its index
        if letter == guess:
            display[index] = guess
            correct_guess = True

    return correct_guess

def get_guess(guessed_letters):
    while True: # infinite loop - stops when we interrupt it (return)
        if guessed_letters:
            print("Previously guessed letters:", " ".join(sorted(guessed_letters)))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha(): # if the guess is not one letter or is not a letter, reject it
            print("Please enter a single alphabetical letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed this letter, try another one :)")
            continue  # skip the rest of this loop iteration and start the next round

        guessed_letters.add(guess)
        return guess

def play_game():
    while True:
        main()

        while True:
            replay = input("Do you want to play again? (y/n): ").lower()

            if replay in ("y", "n"):
                break

            print("Please enter y or n.")

        if replay == "n":
            print("Thank you for playing!")
            break

def main():
    # initial game state
    chosen_word = random.choice(word_list)
    lives = 6
    display = ["_"] * len(chosen_word)

    print(welcome_art)
    display_board(lives, display)

    guessed_letters = set()

    while "_" in display and lives > 0:
        guess = get_guess(guessed_letters)
        correct_guess = process_guess(chosen_word, guess, display)

        if not correct_guess:
            lives -= 1
            print(f"OOPS! Wrong guess. Remaining lives: {lives}/6")

        display_board(lives, display)

    if "_" not in display:
        print("\nCongratulations! You won!")
        print(f"The word was: {chosen_word}")
    else:
        print(stages[0])
        print(f"\nYou lost! The word was: {chosen_word}!")

if __name__ == "__main__":
    play_game()







