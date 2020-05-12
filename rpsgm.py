import random
gamelist=["rock","paper","scissors"]

randomresult=random.choice(gamelist)
#print(randomresult)
def decision(randomresult,userquess):
    randomresult=randomresult
    userquess=userquess

    if userquess=="rock" and randomresult=="paper":
        return "computer win"
    elif userquess=="rock" and randomresult=="scissors":
        return "user win"
    elif userquess == "rock" and randomresult == "rock":
        return "draw"
    elif userquess == "paper" and randomresult == "rock":
        return "user win"
    elif userquess == "paper" and randomresult == "scissors":
        return "computer win"
    elif userquess == "paper" and randomresult == "paper":
        return "draw"
    elif userquess == "scissors" and randomresult == "paper":
        return "user win"
    elif userquess == "scissors" and randomresult == "rock":
        return "computer win"
    elif userquess == "scissors" and randomresult == "scissors":
        return "draw"

while True:
    userquess=input("Please write your choose *rock *paper*scissors\n")
    if userquess not in gamelist:
        print("please write valid quess")

    result=decision(randomresult,userquess)
    print("Choosing of computer ", randomresult)
    print(result)

    answer=input("Do you  want to continue  for yes  write 'y' for no write 'n'")
    if answer=="n":
        break
