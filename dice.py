
from random import randint

class Dice:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0

    def roll(self):
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        return dice1, dice2

    def play(self):
        score1 = self.score1
        score2 = self.score2
        for i in range(3):
            rolled1 = self.roll()
            rolled2 = self.roll()
            score1 += sum(rolled1)
            score2 += sum(rolled2)
                
            if rolled1 == (1,1) or rolled2 == (1,1):
                break
            print(self.player1,'had', rolled1, 'and', self.player2, 'had', rolled2)
            play_again = input("Do you want to play again? (yes or no) ")
            if play_again == 'yes':
                continue
            else:
                break
        print(self.player1,'had', score1, 'and',self.player2,'had', score2)
        if score1 > score2: print('winner is:', self.player1)
        else: print('winner is: ', self.player2)

player1 = input('enter name of player1: ')
player2 = input('enter name of player2: ')


game = Dice(player1, player2)
game.play()
