import random
import time

def computerchoice():
    return random.choice(["rock","paper","scissor"])

def getresult(cc,uc):
    if cc==uc:
        return "draw"
    elif(uc == "scissor" and cc == "paper") or (uc == "rock" and cc == "scissor") or (uc == "paper" and cc == "rock"):
        return "user"
    else:
        return "computer"
    
def showresult(cc,uc,re):
    print("Your choice : ",uc)
    print("Computer's choice : ",cc)
    time.sleep(1)
    if re == "deaw":
        print("The game was tie..\n")
    elif re == "user":
        print("Congrats you won the game.\n")
    else:
        print("Oops:( the computer won the game.\n")


us = 0
cs = 0
print("Welcome to the Rock Paper Scissor game..")

while True:
    time.sleep(1)
    UserChoice = input("""Enter your choice from..:
                       1. Rock
                       2. Paper
                       3. Scissor
                       4. Quit
                       """).lower()
    if UserChoice not in ["rock","paper","scissor","quit"]:
        print("The choice you entered is invalid.")
    if UserChoice == "quit":
        print("Thanks for playing the game")
        break

    ComputerChoice = computerchoice()
    result = getresult(ComputerChoice,UserChoice)
    showresult(ComputerChoice,UserChoice,result)

    if result == "user":
        us +=1
    elif result == "computer":
        cs +=1    
    time.sleep(1)
    print("Calculating....")
    time.sleep(1)
    print(f"""Scores :
          Your score : {us}
          Computer score : {cs}""")
    again = input("Wanna try again..! : ").lower()
    if again == "no":
        print("Thanks for playing the game.\nYou made a great play..!")
        break