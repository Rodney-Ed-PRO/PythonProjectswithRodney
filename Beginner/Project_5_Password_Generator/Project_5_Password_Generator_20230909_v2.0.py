#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password_letters = ""
for letter in range(0,nr_letters):
  r = random.randint(0,51)
  password_letters += letters[r]

password_numbers = ""
for number in range(0, nr_numbers):
  n = random.randint(0,9)
  password_numbers += numbers[n]

password_symbols =""
for symbol in range(0, nr_symbols):
  s = random.randint(0,8)
  password_symbols += symbols[s]

print("\nHere is an easy password: " + password_letters + password_symbols + password_numbers + "\n")  

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_password = []
for letter in range(0,nr_letters):
  r = random.randint(0,51)
  hard_password.append(letters[r])

for number in range(0, nr_numbers):
  n = random.randint(0,9)
  hard_password.append(numbers[n])

for symbol in range(0, nr_symbols):
  s = random.randint(0,8)
  hard_password.append(symbols[s])
# Shuffle the items in the list in random order using the random.shuffle() function
random.shuffle(hard_password)
# Convert the shuffled list of items in the hard_password list into a string
# for i in hard_password:
#   print(i, end = "")
hard_password_as_string =""
for i in hard_password:
  hard_password_as_string += i
print(hard_password)
print("Here is a difficult password: " + hard_password_as_string)
# data type check
print(type(hard_password_as_string))

# Another way to generate a password with user criteria in random order
password_characters = ""
for letter in range(0,nr_letters):
  r = random.randint(0,51)
  password_characters += letters[r]

for number in range(0, nr_numbers):
  n = random.randint(0,9)
  password_characters += numbers[n]

for symbol in range(0, nr_symbols):
  s = random.randint(0,8)
  password_characters += symbols[s]

hard_password2 = ''.join(random.sample(password_characters,len(password_characters)))

print("\nHere is another hard password that was generated differently: " + hard_password2)
