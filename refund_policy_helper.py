import os 
os.system("cls")

Q1=input('How many days ago have you purchased the item? ')
Q2=input('Have you used the item at all ? y/n ')
Q3=input('Has the item broken down on its own ? y/n ')
if(Q3=='y' or int(Q1)<=10 and Q2=='n'):
    print('You can get a refund')
else:
    print('You cannot get a refund')