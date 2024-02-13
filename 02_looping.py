# main routine starts here



# set maximum numbr of tickets below
max_tickets = 3

# loop to sell tickets

tickets_sold = 0

while tickets_sold < max_tickets:
    name = input("Please enter your name or 'xxx' to quit: ")

    if name == "xxx":
        break

    tickets_sold += 1




# output number of tickets sols

if tickets_sold == max_tickets:
    print("Congratulations you have sold all the tickets")

else:
    print(f"You have sold {tickets_sold} tickets. There is {max_tickets - tickets_sold} tickets remaining")
