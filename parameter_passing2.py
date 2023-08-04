# 4) Variable Length Positional Arguement
## Q) Write a function to add multiple elements at a time and create a list

import os
os.system("cls")

# l=[100,200,300,400,500]
# l.append(600)
# print(l)
# l.append(10,20,30)
# print(l)

# def add_values(*args):
 #   for value in args:
  #      l.append(value)
  #  return l

# l=[100,200,300,400,500]
# result=add_values(10,20,30)
# print(result)


# 5) Variable Length Keyword Arguement
## Q) Entering of name, email, contact & DOB in a form (max 4 fields can be entered, but less than that are also acceptable)

def get_details(**kwargs):
    print(kwargs)

result=get_details(email="abc@gmail.com",contact="098765567890",dob="23-12-1997")
result=get_details(name="ABC",email="abc@gmail.com",dob="23-12-1997")
result=get_details(name="ABC",contact="098765567890",dob="23-12-1997")
# print(result)