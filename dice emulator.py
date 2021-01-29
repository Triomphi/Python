'''A class to simulate a dice emulator'''

from random import randint
import time as t

class DiceEmulator:
    # Initializing the attributes of the instances
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0
        self.score_sheet = {}
    
    def roll_die(self):
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        return dice1, dice2
    
    def score_board(self):
        '''This method determines the winner based on their scores'''
        score1 = self.score1
        score2 = self.score1
        score_sheet = self.score_sheet
        score_sheet = sorted(score_sheet.items(), key = lambda x : x[1])
        winner_name = score_sheet[-1][0]
        winner_score = score_sheet[-1][-1]
#         sort_score = sorted((list((score1, score2))))
        print('\nAnd the winner is...')
        t.sleep(2)
        print(f'{winner_name} with {winner_score} points! \n\nCongratulations {winner_name}')
   
    def players(self):
        start = 0
        stop = 4
        score1 = self.score1
        score2 = self.score2
        while start < stop:
            rolled1 = self.roll_die()
            rolled2 = self.roll_die()
            play1 = rolled1
            score1 += sum(play1)
            play2 = rolled2
            score2 += sum(play2)
            
            print(f'\n{self.player1} rolled {play1} and {self.player2} rolled {play2}')
            if play1 == (1,1) or play2 == (1,1):
                break
            start += 1
            print('\nDo you want to roll again? y or n?')
            again = input('> ').lower()
            if again == 'n':
                break
            elif again == 'y':
                continue
        self.score_sheet.update({self.player1:score1, self.player2:score2})
        print(f'{self.player1} scored {score1} points while {self.player2} scored {score2} points')
        self.score_board()
        
player1 = input('Enter a name for player1: ')
player2 = input('Enter a name for player2: ')

a = DiceEmulator(player1, player2)
a.players()