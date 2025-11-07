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
game_image=[rock,paper,scissors]
choice=int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors\n"))
print(game_image[choice])

print("computer choice")
rand=random.randint(0,2)
print(game_image[rand])


if choice >=3 or choice < 0:
    print("invalid choice")
elif choice == 0  and  rand == 2:
    print("you win")
elif choice == 1 and rand == 2:
    print("you lose")
elif choice == 0  and rand == 1:
    print("you lose")
elif choice == rand:
    print("draw")
