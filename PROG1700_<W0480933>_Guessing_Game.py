import random 


#defining the computer chosen number as a random integer 
compnumber= random.randint(0, 10)
tries = 0
   #uses a range of user tries, limiting the user to 5
for tries in range(5):
    userguess = int(input("pick a number from one to ten!: "))
    tries += 1
#for every try adding one turn to the variable
   
   #game win conditions, if the user guesses the number they win
    if userguess == compnumber and tries <= 5:
        print("you won!, You guessed it in", tries, "tries!, please play again")
        break
  
    elif userguess > compnumber and tries < 5:
        print("too high! try again :(")
        tries += 1
        #if the userguess is too high use a turn and print too high
    elif userguess < compnumber and tries < 5:
        print("too low! try again :(")
        tries += 1
     #if the userguess is too low use a turn and print too low
  
  
  #if the user exceeeds 5 turns you lose
    elif tries >= 5:
        print("you lose :(") 


