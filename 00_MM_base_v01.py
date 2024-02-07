# functions go here

# checks users enter an integer to a given question
def num_check(question):
    while True:
        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer")



# Checks user has entered yes / no to a question
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter yes or no")



# Calculates the ticket price based on the age
def calculate_ticket_price(var_age):

    # ticket is $7.50 for users under 16

    if var_age < 16:
        price = 7.5

    # ticket is $10.50 for users between 16 and 64

    elif var_age < 65:
        price = 10.5

    # price is #6.50 for users 65+(seniors)
    else:
        price = 6.5

    return price

# checks that user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("Sorry this cant be blank. Please try again")
        else:
            return response








# main routine starts here



# set maximum numbr of tickets below
max_tickets = 3
tickets_sold = 0


# Ask user if they want to see the instructions
want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes" or want_instructions == "y":
    print("Show instructions")


# loop to sell tickets



while tickets_sold < max_tickets:
    name = not_blank("Enter your name (or 'xxx' to quit): ")

    if name == "xxx":
        break

    age = num_check("Age: ")

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("Sorry your too young for this movie")
        continue
    else:

        print("That looks like a typo, please try again")
        continue

    # calculate the ticket cost

    ticket_cost = calculate_ticket_price(age)

    print(f"Age: {age}, Ticket Price: ${ticket_cost:.2f}.")

    tickets_sold += 1
    print("Ticket Sold!")




# output number of tickets sols

if tickets_sold == max_tickets:
    print("Congratulations you have sold all the tickets")

else:
    print(f"You have sold {tickets_sold} tickets. There is {max_tickets - tickets_sold} tickets remaining")