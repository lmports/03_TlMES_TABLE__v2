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
