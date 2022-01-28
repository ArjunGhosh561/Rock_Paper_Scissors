
from random import randint


def replay():
    return input("Do you want to play again? Y or N:").lower().startswith('y')


print("LETS PLAY ROCK PAPER SCISSORS :)")
moves = [' rock','paper',' scissors']

while True:
    computer = moves[randint(0,2)]
    player = input("ROCK PAPER OR SCISSORS?->").lower()
    if player == computer:
        print("TIE!", computer, "and ", player, "are same *_*")
    elif player == 'paper':
        if computer == 'scissors':
            print("YOU LOOSE T_T", computer, "beats", player)
        else:
            print("YOU WIN", player, "beats", computer)
    elif player == 'rock':
        if computer == 'paper':
            print("You loose T_T", computer, "beats", player)
        else:
            print("YOU WIN :)", player, "beats", computer)
    elif player == 'scissors':
        if computer == 'rock':
            print("You loose T_T", computer, "beats", player)
        else:
            print("YOU WIN :)", player, "beats", computer)
    else:
        print("CHECK YOUR SPELLING")

    if  not replay():
        print("The game has ended")
        break
