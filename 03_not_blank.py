# functions goes here








# checks that user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("Sorry this cat be blank. Please try again")
        else:
            return response




while True:
    name = not_blank("Enter your name (or 'xxx' to quit): ")

    if name == "xxx":
        break