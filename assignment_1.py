from datetime import datetime
customer = input("Enter your full name: ")
print("Welcome to our cinema " + customer)
customer_age = datetime.now().year - int(input("Enter your birth year: "))
if customer_age >= 18:
    print("You are eligible to watch the movie")
    ticket_enquiry = input("Do you have the movie  ticket? (yes/no): ")
    if ticket_enquiry.lower() == "yes":
        ticket_number = input("Please enter your ticket number: ")
        print("Ticket number verified. Enjoy the movie " + customer + "!")
    else:
        print("You need to purchase a ticket before entering the cinema.")
else:
    print("You are under 18 years old. You must be accompanied by a parent or guardian to watch this movie")
