import random
print("Rock paper Scissor Game")
print("Write Rock or Paper or scissor to play and break to stop the game")
youwin = 0
computerwin = 0
while True:
    users = input(f"Rock,paper,scissor ?")
    random_number = random.randint(1, 3)
    if users.lower()=='break':
        break
    if random_number == 1:
        randomuser = 'rock'
    elif random_number == 2:
        randomuser = 'paper'
    elif random_number == 3:
        randomuser = 'scissor'
    else:
        print('value not found')
    user = users.lower()
    if user == 'rock':
        user = 1
    elif user == 'paper':
        user = 2
    elif user == 'scissor':
        user = 3
    else:
        print("wrong input")

    print(randomuser)


    def rock():
        if random_number == 1 and user == 1:
            print('Draw')
        elif random_number == 1 and user == 2:
            print('You win')
        elif random_number == 1 and user == 3:
            print('Computer win')


    def paper():
        if random_number == 2 and user == 1:
            print('Computer win')
        elif random_number == 2 and user == 2:
            print('Draw')
        elif random_number == 2 and user == 3:
            print('You win')


    def scissor():
        if random_number == 3 and user == 1:
            print('You win')
        elif random_number == 3 and user == 2:
            print('Computer Wins')
        elif random_number == 3 and user == 3:
            print('Draw')



    if random_number == 3 and user == 1 or random_number == 2 and user == 3 or random_number == 1 and user == 2:
            youwin = youwin + 1
    elif random_number == 3 and user == 2 or random_number == 2 and user == 1 or random_number == 1 and user == 3:
            computerwin = computerwin + 1


    rock()
    paper()
    scissor()

print(f"computer have won {computerwin} times")
print(f"you have won {youwin} times")



