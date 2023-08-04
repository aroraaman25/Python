# WAP to count the number of even and odd numbers from a series of numbers
# Sample numbers: 1,2,3,4,5,6,7,8,9

import os
os.system("cls")
even=0
odd=0
for value in range(1,10):
	if value%2==0:
		# print(value, "is an even number")
		even=even+1
	else:
		# print(value, "is an odd number")
		odd=odd+1

print("Count of Even Numbers is", even)
print("Count of Odd Numbers is", odd)