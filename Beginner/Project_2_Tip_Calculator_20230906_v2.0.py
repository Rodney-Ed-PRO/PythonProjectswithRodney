# This program will calculate the bill with tip split amongst a group of people
# Print the welcome message
print("Welcome to the Tip Calculator!")
# Ask the user for the total bill
total_bill = float(input("What was the total bill? $"))
# Ask the user to enter the desired tip percentage
tip_percent = 1 + float(input("What percentage tip would you like to give? "))/100
# Ask the user for the number of people the bill is being split amongst
number_of_people = int(input("How many people are you splitting the bill with? "))
# Calculate the bill per person including tips
bill_per_person = (total_bill*tip_percent)/number_of_people
# Type a message for the bill per person
message = f"Each person should pay: ${round(bill_per_person,2)}"
# print message
print(message)
