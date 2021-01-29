import random

def intro():
     name = input("what is your name?")
     print("Hello {} welcome to the math quiz".format(name))

def generate_random_number():
     num_1 = random.randint(1,10)
     num_2 = random.randint(1,10)
     return num_1, num_2

def endgame():
    print("do you wnt to continue? (y/n)")
    choice = input()
    return choice

def main():
    intro()

    while True:
        num_1, num_2 = generate_random_number()
        correctAnswer = num_1 + num_2
        users_answer = int(input("{} + {} =".format(num_1, num_2)))
        if users_answer == correctAnswer:
            print("good job")

        else:
            while users_answer != correctAnswer:
                print("try again")
        
                users_answer = int(input("{} + {} =".format(num_1, num_2)))
            print("good job")
        response = endgame()
        if response == 'n':
            print("goodbye")

main()
        
        


    
