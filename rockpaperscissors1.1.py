

import random

 

options = ["Rock", "Paper", "Scissors"]

 

user_choice = input(" Rock, Paper,Scissors: ")

computer_choice = random.choice(options)

 

print("You picked: ", user_choice)

print("Computer picked: ", computer_choice)

 

if user_choice == computer_choice:

    print("It's a tie!")

elif user_choice == "Rock" and computer_choice == "Scissors":

    print("You win!")

elif user_choice == "Paper" and computer_choice == "Rock":

    print("You win!")

elif user_choice == "Scissors" and computer_choice == "Paper":

    print("You win!")

else:

    print("Computer wins :(")


 





