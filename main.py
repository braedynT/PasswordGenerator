
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the ByPassword Generator! 2 Free Random passwords!")
userlet = int(input("How many letters would you like?\n")) 
usernum = int(input(f"How many numbers would you like?\n"))
usersym = int(input(f"How many symbols would you like?\n"))

password = [""]

for let in range(1,userlet + 1):
  password += random.choice(letters)
for num in range(1, usernum + 1):
  password += random.choice(numbers)
for sym in range(1, usersym + 1):
  password += random.choice(symbols)
random.shuffle(password)
passwordnew = ""
for characters in password:
  passwordnew += characters
print(f"Your password is: {passwordnew}")