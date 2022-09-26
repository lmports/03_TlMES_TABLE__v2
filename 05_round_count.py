import random

#main routine goes here

STARTING_BALANCE = 100

balance = STARTING_BALANCE

for item in range(0,100):
    chose_num = random.randint(1,100)


    if 1 <= chose_num <= 5:
        chosen = "unicorn"
        balance += 4

    elif 6 <= chose_num <= 36:
        chosen = "donkey"
        balance -= 1


    else:

        if chose_num % 2 == 0:
            chosen = "horse"


        else:
            chosen = "zebra"

        balance -= 0.5
