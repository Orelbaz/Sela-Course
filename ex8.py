import sys

#asking for the players to choose the play they want (rock ,paper ,scissors)
player1 = input("Lets play Rock ,Paper ,Scissors: ")
if player1 in ("rock ,paper ,scissors"):
    pass
else:
    input("You must choose rock ,paper ,scissors")
sys.exit

player2 = input("Lets play Rock ,Paper ,Scissors: ")
if player2 in ("rock ,paper ,scissors"):
    pass
else:
    input("You must choose rock ,paper ,scissors")
sys.exit

#printing the results of the game
if player1 == "rock" and player2 == "paper": 
    print("player2 Win!")
if player1 == "rock" and player2 == "scissors":
    print("player1 Win!")
if player1 == "paper" and player2 == "rock":
    print("player1 Win!")
if player1 == "paper" and player2 == "scissors":
    print("player2 Win!")
if player1 == "scissors" and player2 == "rock":
    print("player2 Win!")
if player1 == "scissors" and player2 == "paper":
    print("player1 Win!")

if player1 == player2:
    print("Teko Teko")


