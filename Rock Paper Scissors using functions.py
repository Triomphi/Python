
import random

RPS = ['rock', 'paper', 'scissors']

def intro():
    print("hello welcome to the game : Rock, Paper, Scissors")

def users_choice():
    print("... your turn")
    choice = input()
    return choice

def computers_choice():
    chosen = random.choice(RPS)
    return chosen

def main():
    intro()

    tie = [['rock','rock'],['paper','paper'],['scissors','scissors']]
    win = [['rock','scissors'],['paper','rock'],['scissors','paper']]
    loss = [['scissors','rock'],['rock','paper'],['paper','scissors']]

    no_of_play = 0
    winner = 0
    loser = 0
    draw = 0
    
    while no_of_play <5:
        
        chosen = computers_choice()
        choice = users_choice()
        answer = [choice,chosen]
            
        if answer == win[0] or answer == win[1] or answer == win[2]:
            print("you won")
            winner += 1

        elif answer == loss[0] or answer == loss[1] or answer == loss[2]:
            print("you lost")
            loser += 1

        else:
            print("its a tie")
            draw += 1                
            
        no_of_play += 1
    print("you won {} times".format(winner))
    print("you lost {} times".format(loser))
    print("there were {} ties".format(draw))
          
main()        
        

    
    
