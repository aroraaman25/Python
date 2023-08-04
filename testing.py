#Entering n number of arguements at a time in a list and create a new list

import os
os.system("cls")

def add_args(*args):
    for value in args:
        l.append(value)
    return l

l=[50,100,150,200,250]
# l.append(10)
# print(l)
result=add_args(10,20,30,40)
# print(result)

num=6
result=num%3
print(result)


