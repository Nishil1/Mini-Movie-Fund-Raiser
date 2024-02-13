import pandas
import random
from datetime import date


# functions go here

# checks users enter an integer to a given question
def num_check(question):
    while True:
        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer")


# show instructions
def show_instructions():
    print('''\n
    
***** Instructions *****

For each ticket, enter ...

- The person's name(can't be blank)
- Age (between 12 and 120)
- Payment method (cash / credit)

When you have entered all the users, press 'xxx' to quit.

The program will then display the ticket details including the cost
of each ticket, the total cost and the total profit.
 
 
 This information will also be automatically written to a text file.

    ''')


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


# checks that users enter a valid response (eg yes / no, cash / credit based on  a list of options
def string_checker(question, short_version, valid_response):
    error = f"Please choose {valid_response[0]} or {valid_response[1]}"

    while True:
        response = input(question).lower()

        for item in valid_response:
            if response == item[:short_version] or response == item:
                return item
        print(error)


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# main routine starts here


# set maximum number of tickets below
max_tickets = 5
tickets_sold = 0

yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# dictionaries to hold ticket details

all_names = []
all_ticket_costs = []
all_surcharge = []

# Dictionary used to create data frame
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}

# Ask user if they want to see the instructions
want_instructions = string_checker("Do you want to read the instructions? ", 1, yes_no_list)

if want_instructions == "yes" or want_instructions == "y":
    show_instructions()

# loop to sell tickets
while tickets_sold < max_tickets:
    name = not_blank("Enter your name (or 'xxx' to quit): ")

    if name == "xxx" and len(all_names) > 0:
        break
    elif name == 'xxx':
        print("You must sell at least ONE ticket before quitting")
        continue

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

    # get payment method
    pay_method = string_checker("Choose a payment method(cash / credit): ", 2, payment_list)

    if pay_method == "cash":
        surcharge = 0
    else:
        # 5% surcharge
        surcharge = ticket_cost * 0.05

    tickets_sold += 1

    # add ticket name, cost and surcharge to lists
    all_names.append(name)
    all_ticket_costs.append(ticket_cost)
    all_surcharge.append(surcharge)

mini_movie_frame = pandas.DataFrame(mini_movie_dict)
# mini_movie_frame = mini_movie_frame.set_index('Name')

# Calculate the total ticket cost (ticket + surcharge)

mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

# calculate the profit for each ticket

mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# calculate ticket and profit totals

total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# choose winner and look up total won
winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']

# Currency Formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# set index at end (before printing)
mini_movie_frame = mini_movie_frame.set_index('Name')

# ***** Get current date for heading and file name *****

# Get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

heading = f"----- Mini Movie Fundraiser Ticket data ({day}/{month}/{year}) -----\n"
filename = f"MMF_{year}_{month}_{day}"

print()

# Change frame to a string so that e can export it to file
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

# Create string for printing / writing to file....
ticket_cost_heading = "\n ----- Ticket Cost / Profit -----"
total_ticket_sales = "Total Ticket Sales ${:.2f}".format(total)
total_profit = "Total Profit: ${:.2f}".format(profit)

winner_heading = "\n ----- Raffle Winner -----"
winner_text = "The winner of the raffle is {}. " \
              "They have won ${:.2f}. ie: Thier ticket is free!".format(winner_name, total_won)

# list holding content to print / write to file
to_write = [heading, mini_movie_string, ticket_cost_heading, total_ticket_sales, total_profit,
            winner_heading, winner_text]

# print output
for item in to_write:
    print(item)

print()

# display how many tickets are sold, all or display amount unsold and say how many have been sold
if tickets_sold == max_tickets:
    print("Congratulations you have sold all the tickets")

else:
    print(f"You have sold {tickets_sold} out of {max_tickets} tickets. "
          f"There is {max_tickets - tickets_sold} tickets remaining")

# write output to file
# create file to hold data (add .txt extension)
write_to = f"{filename}.txt"
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()
