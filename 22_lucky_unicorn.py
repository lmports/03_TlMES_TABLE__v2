show_instructions = input("Have you played Lucky Unicorn before?") .lower()

if show_instructions.lower() == "yes" :
    print("Program continues")

elif show_instructions.lower() == "y" :
    print("Display Instructions")

elif show_instructions.lower() == "no" :
    print("Display Instructions")

elif show_instructions.lower() == "n" :
    print("Display Instructions")

else:
    print("please enter yes or no")
