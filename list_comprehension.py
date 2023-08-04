import os 
os.system("cls")

## NOTE: In comprehension, whatever output we want, we mention that at the start of the list
## NOTE: List Comprehension can be used where there is a need to perfom the same operation at each element

# Q) To square the elements of the list and store them in another list
#l=[100,200,300,400,500]
#l2=[]

#for value in l:
#    l2.append(value*value)
#print(l2)

#l3=[value*value for value in l]
#print(l3)

# Q) Suppose there is a list and we have to print only the even numbers from it
#l=[10,20,35,48,55,67,80,94]
#l2=[value%2==0 for value in l]
#print(l2)
#l3=[value for value in l if value%2==0]
#print(l3)

# Q3) To store the length of each element in another list
l=['ab','abc','abcd','abcde']
l2=[len(value) for value in l]
print(l2)