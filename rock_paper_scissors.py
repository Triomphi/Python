
import random

RPS = ['rock', 'paper', 'scissors']

    tie = [['rock','rock'],['paper','paper'],['scissors','scissors']]
    win = [['rock','scissors'],['paper','rock'],['scissors','paper']]
    loss = [['scissors','rock'],['rock','paper'],['paper','scissors']]

    no_of_play= 0
    wins= 0
    losses = 0
    ties = 0


    while no_of_play <5:
        computer_choice = random.choice(RPS)
        user_choice = input("your turn: ")

        

        result = [user_choice, computer_choice]

        if result == win[0] or result == win[1] or result == win[2]:
            print("you won")
            wins += 1

        elif result == loss[0] or result == loss[1] or result == loss[2]:
            print("you lost")
            losses += 1

        else:
            print("its a tie")
            ties += 1
        no_of_play += 1
print("you won {} times".format(wins))
print("you lost {} times".format(losses))
print("there were {} ties".format(ties))
      
       
