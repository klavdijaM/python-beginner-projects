import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("Let's play rock, paper, scissors! What do you choose? Type 0 for rock, 1 for paper or 2 for scissors :)\n"))
if user_choice == 0:
    print("You chose:")
    print(rock)
elif user_choice == 1:
    print("You chose:")
    print(paper)
elif user_choice == 2:
    print("You chose:")
    print(scissors)
else:
    print("Please pick a valid number and try again")

computer_choice = random.randint(0,2)
if computer_choice == 0:
    print("Computer chose: ")
    print(rock)
elif computer_choice == 1:
    print("Computer chose: ")
    print(paper)
elif computer_choice == 2:
    print("Computer chose: ")
    print(scissors)

