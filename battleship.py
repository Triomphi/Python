from random import randint
sea = []
trial = 4
head = 0 

for _ in range(10):
    sea.append('0 '*10)
def sea_board(sea):
    for row in sea:
        print(row)
def computer_row(sea):
    return randint(0, (len(sea)-1))
def computer_column(sea):
    return randint(0, (len(sea)-1))
row = computer_row(sea)
column = computer_column(sea)

no_trials = 3
for i in range(trial):
    user_row = int(input('guess the row: '))
    user_column = int(input('guess the column: '))
    print('')
    if user_row == row and user_column == column:
        print('you sunk the ship')
        break
    elif user_row == row:
        print('you got the row right')
        print('you have {} guesses left'.format(no_trials))
    elif user_column == column:
        print('you got the column right')
        print('you have {} guesses left'.format(no_trials))
    else:
        print('you guessed wrongly')
        print('you have {} guesses left'.format(no_trials))
    no_trials -= 1
    sea_board(sea)
    