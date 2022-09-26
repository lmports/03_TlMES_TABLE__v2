
show_instructions = ""

while show_instructions != "xxx" :

    show_instructions = input("have you played Lucky Unicorn before?")

    if show_instructions == "yes" or show_instructions == "y" :
        print("program continues")

    elif show_instructions == "no" or show_instructions == "n" :
        print("Display Instructions")

    else:
        print("please enter yes or no")
