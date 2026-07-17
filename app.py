from datetime import datetime
print("Hello World!")
print("*" * 10)
# age = 20
# print (age)
price = 19.24
print(price)


patient_name = "John Smith"
patient_age = 20
is_new_patient = True
print(patient_name + " is " + str(patient_age) +
      " and is a new patient: " + str(is_new_patient))

first_name = input("First: ")
last_name = input('last:')
print('Hello ' + first_name + " " + last_name + " welcome to Python Tutorial ")
birth_year = input("Enter your birth year: ")
dob = datetime.now().year - int(birth_year)
print(dob)
