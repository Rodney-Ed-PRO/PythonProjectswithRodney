# This program will calculate the bill with tip split amongst a group of people
# Print the welcome message
print("Welcome to the Tip Calculator!")
# Ask the user for the total bill
total_bill = input("What was the total bill? ")
# Ask the user to enter the desired tip percentage
tip_percent = input("What percentage tip would you like to give? ")
# Ask the user for the number of people the bill is being split amongst
number_of_people = input("How many people are you splitting the bill with? ")
# Convert user inputs into numerical data types
total_bill_float = float(total_bill)
tip_percent_float = 1 + float(tip_percent)/100
number_of_people_int = int(number_of_people)
# Calculate the bill per person including tips
bill_per_person = (total_bill_float*tip_percent_float)/number_of_people_int
# Type a message for the bill per person
message = f"Each person should pay: ${round(bill_per_person,2)}"
# print message
print(message)
