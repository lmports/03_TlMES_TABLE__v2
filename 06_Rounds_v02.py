import random

balance = 5


rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":


    rounds_played += 1


    print()
    print("*** Round #{} ***".format(rounds_played))
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


    play_again = input("Press Enter to play again" "or 'xxx' to quit")


    if balance <1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again



