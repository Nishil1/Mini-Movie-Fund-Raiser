import pandas

# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# dictionaries to hold ticket details

all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": surcharge
}

mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Calculate the total cost (ticket + surcharge)

mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

# calculate the profit for each ticket

mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Currency Formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

print(mini_movie_frame)

# calculate ticket and profit totals
total_sales = mini_movie_frame['Ticket Price'].apply(lambda x: float(x[1:])).sum() + mini_movie_frame['Surcharge'].apply(lambda x: float(x[1:])).sum()
profit_total = mini_movie_frame['Profit'].apply(lambda x: float(x[1:])).sum()

# output total ticket sales and profit
print(f"Total Ticket Sales: {currency(total_sales)}")
print(f"Total Profit: {currency(profit_total)}")
