# checks that users enter a valid response (eg yes / no, cash / credit based on  a list of options

def string_checker(question, short_version, valid_response):

    error = f"Please choose {valid_response[0]} or {valid_response[1]}"


    while True:
        response = input(question).lower()

        for item in valid_response:
            if response == item[:short_version] or response == item:
                return item
        print(error)


valid_pay = ("cash", "credit")
valid_yes_no = ("yes", "no")

choice = string_checker("cash or credit: ", 2, valid_pay)
print(f"You chose {choice}")
coffee = string_checker("Like coffee? ", 1, valid_yes_no)
print(f"You chose {coffee}")

