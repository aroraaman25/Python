# 1) Positional Arguement: If total number of arguements in a func def & func call is same, then this type of system is called Positional Arguement System

import os
os.system("cls")

# def linear_search(l,key):
#    for value in l:
#        if key==300:
#            return True
#    else:
#            return False
# l=[100,200,300,400,500]
# key=3000
# result=linear_search(l,key)
# print(result)


# 2) Default Arguement: 
## Q) I want a password generator, that generates a new password everytime with 1 UC, 1 LC, 1 SC & 5 digits

# print(ord('a'), ord('z')) ------ prints the ASCII number of alphabets
# print(ord('A'), ord('Z')) 
# print(chr(97))

# import random
# l=["@","#","$","%","&"]
# def generate_password(length=8):
  #  upper = chr(random.randint(65,90))
  #  lower = chr(random.randint(97,122))
  #  special = random.choice(l)
  #  digit = str(random.randint(10000,99999))
  #  password = upper+lower+special+digit
  #  l0 = random.sample(password,length)
  #  password = ("").join(l0)
  #  return password

# result = generate_password(3)
# print(result)


# 3) KeyWord Arguement:
## Q) Write a function to validate a username & password

def validate(username,password):
    if username =="abc" and password =="ABC@123":
        print("Valid Password")
    else:
        print("Invalid Password")

result=validate("abc","ABC@123")
