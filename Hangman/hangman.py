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
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed this letter, try another one :)")
            continue  # skip the rest of this loop iteration and start the next round

        guessed_letters.add(guess)
        return guess

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
            print(f"OOPS! Wrong guess. Remaining lives: {lives}")

        display_board(lives, display)

    if "_" not in display:
        print("\nCongratulations! You won!")
        print(f"The word was: {chosen_word}")
    else:
        print("\nSorry, you lost!")
        print(stages[0])
        print(f"The word was: {chosen_word}")

if __name__ == "__main__":
    main()







