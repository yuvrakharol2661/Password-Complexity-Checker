import re

pas = input("Enter Password: ")
strength = 0
if len(pas) >= 8:
    strength += 1
if re.search("[A-Z]", pas):
    strength += 1
if re.search("[a-z]", pas):
    strength += 1
if re.search("[0-9]", pas):
    strength += 1
if re.search("[@#$%^&*!]", pas):
    strength += 1
if strength == 5:
    print("Strong Password")
elif strength >= 3:
    print("Medium Password")
else:
    print("Weak Password")
