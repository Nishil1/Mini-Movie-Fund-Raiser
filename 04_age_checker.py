# functions go here


# checks users enter an integer to a given question
def num_check(question):
    while True:
        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer")






# main routine

tickets_sold = 3



while True:

    name = input("name: ")
    if name == "xxx":
        break

    age = num_check("Age: ")

    if 12<= age <= 120:
        pass
    elif age < 12:
        print("Sorry your too young for this movie")
        continue
    else:

        print("That looks like a typo, please try again")
        continue

    tickets_sold += 1

