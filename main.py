import random
choices = {
            "Snake":1,
            "Water":2,
            "Gun":3
}
possible_choices = [1,2,3]
try:
    player_choice = int(input("Enter your choice:-\n1 for Snake\n2 for Water\n3 for Gun\n>>> "))
except:
    print("You Entered a wrong choice! Try Again")
    exit()
computer_choice = random.choice(list(choices.keys()))
if player_choice == 1:
    print("Player chose:- Snake")
elif player_choice == 2:
    print("Player chose:- Water")
else:
    print("Player chose:- Gun")
print(f"Computer chose:- {computer_choice}")
if player_choice == 1 and choices[computer_choice] == 1 or player_choice == 2 and choices[computer_choice] == 2 or player_choice == 3 and choices[computer_choice] == 3:
    print("The Game is a DRAW!")
elif player_choice == 1 and choices[computer_choice] == 2 or player_choice == 2 and choices[computer_choice] == 3 or player_choice == 3 and choices[computer_choice] == 1:
    print("You WIN!")
else:
    print("You LOSE!")