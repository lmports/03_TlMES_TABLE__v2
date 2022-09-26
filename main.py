def num_check(question, low, high):
    error = "please enter a whole number between 1 and 10\n"

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











