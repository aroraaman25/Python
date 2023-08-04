import os 
os.system("cls")

while True:
    ans=int(input('When was the Python released? '))
    if ans > 1994:
        print("It was earlier than that!")
    elif ans < 1994:
        print("It was later than that!")
    else:
        print('Correct!, You did it')

    
