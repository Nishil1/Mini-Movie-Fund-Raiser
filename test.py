# choose a winner from our name list
winner_name = random.choice(all_names)

# get position of winner name in list
win_index = all_names.index(winner_name)

# look up total amount won (ie: ticket price + surcharge)
total_won = mini_movie_frame.at[win_index, 'Total']


print()
print("----- Raffle Winner -----")
print(f"Congratulations {winner_name}. You have won ${total_won} ie. your ticket is free! ")

