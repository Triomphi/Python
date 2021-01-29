
import random
import time

def displayIntro():
    print("""you are in a land full of dragons. in front of you,
you see two caves. in one cave, the dragon is friendly
and will share his treasure with you. the other dragon
is greedy and hungry, and will eat you on sight.""")

    print()

def chooseCave():
    cave = ""
    while cave != "1" and cave != "2":
        print("which cave will you go into? (1 or 2)")
        cave = input()

    return cave

def checkCave(chosenCave):
    print("you approach the cave...")
    time.sleep(3)
    print("it is dark and spooky...")
    time.sleep(3)
    print("a large dragon jumps out in front of you! He opens his jaw and ...")
    print()
    
    time.sleep(3)

    computerCave = random.randint(1,2)

    if chosenCave == str(computerCave):
         print("shares his treasure with you")
    else:
        print("Gobbles you down in one bite!")

play_again = "yes"
while play_again == "yes":

    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print("Do you want to play again? (yes or no)")
    play_again = input()

    


