import random

while True:

    play = input("Do you wanna role the dice(y/n)")
    dice = random.randint(1, 6)
    if (play.lower() == "y"):
        print('dice is rolling and you got')
        print(dice)
    elif(play.lower()=="n"):
        print("thanks for playing")
        break
    else:
        print("invalid input")

