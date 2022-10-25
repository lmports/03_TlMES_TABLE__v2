

import random

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower().strip()
        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("please enter yes or no")


def instructions():
    print("**** How to play ****""")
    print()
    print( "!\n""")

    print()
    return ""

def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10"87

    valid = False
    while not valid:
        try:
            response = int(input(question))

            if low < response <= high:
              return response
            else:
                print(error)

        except ValueError:
            print(error)


#Main routine goes here
played_before = yes_no("Have you played te game before?")

if played_before == "no":
    instructions()

print()



how_much = num_check ("how much would you like to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))

balance = how_much


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

    print("You got a {}. Your new balance is {}".format(chosen,balance))
    play_again = input("Press Enter to play again" "or 'xxx' to quit")


    if balance <1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again" "or 'xxx' to quit")


time_table = int(input("what times table do you want to be quizzed on?"))
max_value = int(input("enter the maximum value for your times table"))
score = 0


print("here is the {} times table quiz....good luck".format(time_table))


for x in range(1,max_value+1):

    answer = x * time_table

    guess = int(input("what is {} x {}=".format(x,time_table)))

    if guess == answer:
        print("Correct")
        score +=1

    else:
        print("incorrect, {} x  {}= {}".format(x,time_table, answer))
        print("wrong, please try again")
