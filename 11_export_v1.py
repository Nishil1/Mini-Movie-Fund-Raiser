import pandas
import random
from datetime import date

# lists to hold ticket details
all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {

    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": surcharge

}

# create frame
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

# calculate the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# calculate tickt and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# choose winner and look up total won
winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']


# set index at end (before printing)
mini_movie_frame = mini_movie_frame.set_index('Name')

#***** Get current date for heading and file name *****

# Get today's date
today = date.today()

#Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")


heading = f"The current date is {day}/{month},{year}"
filename = f"MMF_{year}_{month}_{day}"




# Change frame to a string so that e can export it to file
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

# Create string for printing....
ticket_cost_heading = "\n ----- Ticket Cost / Profit -----"
total_ticket_sales = f"Total Ticket Sales ${total}"

total_profit = f"Total Profit: ${profit}"

# edit text below!! It needs to work if he have unsold tickets
sales_status = "\n *** All the tickets have been sold ***"

winner_heading = "\n ----- Raffle Winner -----"
winner_text = f"The winner of the raffle is {winner_name}. "\
                f"They have won ${total_won}. ie: Thier ticket is free!"


to_write = [heading, mini_movie_string, ticket_cost_heading, total_ticket_sales, total_profit, sales_status,
            winner_heading, winner_text]

# print output
for item in to_write:
    print(item)


# wrie output to file
# create file to hold data (add .txt extension)
write_to = f"{filename}.txt"
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()







