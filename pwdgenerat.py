#Just a program that can help you generate a password based on the criteria you give it. You can use it to generat a password to 
# you important assests :)
import random
import string

def generat_password(min_lenght, numbers=True, speci_char=True):
  letters = string.ascii_letters
  digits = string.digits
  special = string.punctuation

  characters = letters
  if numbers:
    characters+= digits
  if speci_char:
    characters+= special 

  pwd = ""
  meet_criteria = False
  has_num = False
  has_speci = False

  while not meet_criteria or len(pwd) < min_lenght:
    new_char = random.choice(characters)
    pwd+= new_char

    if new_char in digits:
      has_num = True
    if new_char in special:
      has_speci = True

    meet_criteria = True
    if numbers:
      meet_criteria = has_num
    if speci_char:
      meet_criteria = meet_criteria and has_speci

  return pwd
while True:
  try:
    min_length = int(input("Please enter the minimum length of the password: "))
  except ValueError:
    print('Please enter a valid number')
  break  

while True:
  hav_numb = input("Would you like the generated password to have numbers? Yes/No: ").lower()
  if hav_numb == 'yes':
    hav_numb == True
    break
  elif hav_numb == 'no':
    hav_numb = False
    break
  else:
    print("Please input in yes or no") 
    continue
while True:
  hav_spec = input("Would you like the generated password to have special characters? Yes/No: ").lower()
  if hav_spec == 'yes':
    hav_spec == True
    break
  elif hav_spec == 'no':
    hav_spec = False
    break
  else:
    print("Please input in yes or no") 
    continue



pwd = generat_password(min_length,hav_numb, hav_spec)
print(pwd)