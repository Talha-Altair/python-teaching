import random

print("hello bro, please play with me")

print("choose:")

print("1.ROCK   2.PAPER  3.SCISSORS")

user_num = int(input())

sample_list = ['ROCK','PAPER','SCISSORS']

random_num = random.randint(0,2)

computer_input = sample_list[random_num]

user_input = sample_list[user_num-1]

print(f"the computer chose {computer_input}")

print(f"you chose {user_input}")

def decide_winner(computer_input,user_input):

    if computer_input == user_input:
        print("ITS A TIE")
        exit()

    if computer_input == 'ROCK':
        if user_input == 'PAPER':
            print('USER WINS')
            exit()
        if user_input == 'SCISSORS':
            print('COMPUTER WINS')
            exit()
    
    if computer_input == 'PAPER':
        if user_input == 'ROCK':
            print('COMPUTER WINS')
            exit()
        if user_input == 'SCISSORS':
            print('USER WINS')
            exit()

    if computer_input == 'SCISSORS':
        if user_input == 'ROCK':
            print('USER WINS')
            exit()
        if user_input == 'PAPER':
            print('COMPUTER WINS')
            exit()



decide_winner(computer_input,user_input)
