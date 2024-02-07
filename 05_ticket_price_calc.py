
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




# calculate the ticket cost

ticket_cost = calculate_ticket_price(age)

print("Age: {}, Ticket Price: ${:.2f}.")