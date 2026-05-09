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

# initial game state
chosen_word = random.choice(word_list)
lives = 6
display = ["_"] * len(chosen_word)

print(welcome_art)
print("Word to guess:", " ".join(display))

# checking user input
while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()

    correct_guess = False

    for index, letter in enumerate(chosen_word): # iterates through each letter and its index
        if letter == guess:
            display[index] = guess
            correct_guess = True

    if not correct_guess:
        lives -= 1
        print(f"OOPS! Wrong guess. Remaining lives: {lives}")
        print("============================================")

    print(stages[lives])
    print("Word to guess:", " ".join(display))

if "_" not in display:
    print("\nCongratulations! You won!")
    print(f"The word was: {chosen_word}")
else:
    print("\nSorry, you lost!")
    print(stages[0])
    print(f"The word was: {chosen_word}")







