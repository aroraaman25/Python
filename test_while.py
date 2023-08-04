import os 
os.system("cls")

secret_number = '10'
user_input=(input('tell me the secret number:' ))
while user_input != secret_number:
    print('Wrong')
    user_input=(input('tell me the secret number:' ))
print('You find it')