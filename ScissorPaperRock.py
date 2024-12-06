import random as rd
list=["scissor","paper","rock"]
def game(userChoice):
    computerChoice=rd.choice(list)
    
    if userChoice in list:
        print("Computer Choice: " + computerChoice+"\n UserChoice: "+userChoice)
        if userChoice==computerChoice:
            print("no one win")
        elif userChoice=="scissor" and computerChoice=="paper":
            print("user win")
        elif userChoice=="rock" and computerChoice=="scissor":
            print("user win")
        else:
            print("Computer wins")
    else:
        print("Give valid input")


userChoice=input("Enter choice:  ")
if(userChoice):
    game(userChoice)