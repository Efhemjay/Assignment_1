from datetime import datetime
# called the module(datetime)inorder to access the current calendar year
customer = input("Enter your full name: ")
# declared a variable(customer) for storing the input data from the user(full name)
print("Welcome to our cinema " + customer)
# this is a welcome message for the user with their name
customer_age = datetime.now().year - int(input("Enter your birth year: "))
# calculated the age of the customer by subtracting the birth year from the current year then store in varaible(customer_age)
if customer_age >= 18:
    # this is a conditional statement to check if the customer is 18 years or older, if true the code block below will be executed
    print("You are eligible to watch the movie")
    # this is the prompt notifying the user of their eligibility to watch the movie
    ticket_enquiry = input("Do you have the movie  ticket? (yes/no): ")
    # this is a prompt asking the user if they have a movie ticket, and the input will be stored in the variable(ticket_enquiry)
    if ticket_enquiry.lower() == "yes":
        # this is a conditional statement to check if the user has a movie ticket, if true the code block below will be executed
        ticket_number = input("Please enter your ticket number: ")
        # this is a prompt asking the user to enter their ticket number, and the input will be stored in the variable(ticket_number)
        print("Ticket number verified. Enjoy the movie " + customer + "!")
        # this is a prompt notifying the user that their ticket number has been verified and they can enjoy the movie
    else:
        # this is a conditional statement to check if the user does not have a movie ticket, if true the code block below will be executed
        print("You need to purchase a ticket before entering the cinema.")
        # this is a prompt notifying the user that they need to purchase a ticket before entering the cinema
else:
    # this is a conditional statement to check if the customer is under 18 years old, if true the code block below will be executed
    print("You are under 18 years old. You must be accompanied by a parent or guardian to watch this movie")
    # this is a prompt notifying the user that they are under 18 years old and must be accompanied by a parent or guardian to watch the movie
