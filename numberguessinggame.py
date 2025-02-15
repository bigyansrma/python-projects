import random
computerguessnum=random.randint(1,100)

while True:
    try:
        guessnumber = int(input('Guess Number between 1 to 100: '))
        if (computerguessnum < guessnumber):
            print("Too High")

        elif (computerguessnum > guessnumber):
            print('Too low')
        else:
            print('you guess it the number is', computerguessnum)
            break
    except:
        print("Invalid Number")




