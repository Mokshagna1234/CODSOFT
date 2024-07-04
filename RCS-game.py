import random

print("<><><>Welcome to Rock-Paper-Scissors game<><><>")

user_score=0
computer_score=0
ties=0

name=input("enter your name: ")
print("""
      Winning Rules: 
      1. Paper vs Rock --> Paper
      2. Rock vs Scissors --> Rock
      3. Scissors vs Paper --> Scissors""")
print()
while True:
    print("""Choices are:
          1. Rock 
          2. Paper
          3. Scissors""")
    choice=int(input("enter your choice from 1-3: "))
    print()
    while choice > 3 or choice < 1:
        choice=int(input("enter valid input"))

    if choice==1:
        user_choice="Rock"
    elif choice==2:
        user_choice="Paper"
    else:
        user_chice="Scissors"

    print("The users choice is", user_choice)
    print("Now it's computer turn")  

    computer=random.randint(1,3) 

    if computer==1:
        comp_choice="Rock"
    elif computer==2:
        comp_choice="Paper" 
    else:
        comp_choice="Scissors" 

    print ("The computer's choice is", comp_choice)
    
    if ((user_choice=="Paper" and comp_choice=="Rock") or(user_choice=="Rock" and comp_choice=="Paper")):
        print("Paper wins")
        result="Paper"
    elif ((user_choice=="Scissors" and comp_choice=="Rock") or(user_choice=="Rock" and comp_choice=="Scissors")):
        print("Rock wins")
        result="Rock"
    elif (user_choice==comp_choice):
        print("it's a tie")
        result="tie"
    else:
        print("Scissors wins")
        result="Scissors" 
    
    if result=="tie":
        ties+=1
    elif result==user_choice:
        print("user wins")
        user_score+=1 
    else:
        print("computer wins")
        computer_score+=1

    print("Scores are")
    print(name,"'s score is", user_score)   
    print("computer's score is", computer_score)
    print("ties are",ties)

    repeat=input("do you want to play again? ")
    if repeat=="No" or repeat=="No":
        break

print("Game over!")
print("Thanks for playing the game!!!")     







