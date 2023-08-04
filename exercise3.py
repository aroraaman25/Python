# WAP which iterates the integers from 1 to 10, For multiples of 3 print "Fizz", for multiples of 5 print "Buzz" 
# & for Multiple of both print "FizzBuzz"

import os
os.system("cls")

num3=0
num5=0
num_both=0
for value in range(1,16):
	if (value%3) == 0 | (value%5) == 0:
		print("FizzBuzz")
		num_both=num_both+1
	elif value%3==0:
		print("Fizz")
		num3=num3+1
	elif value%5==0:
		print("Buzz")
		num5=num5+1
	else:
		print(value)

print("Count of numbers that are multiple of 3 are", num3+num_both)
print("Count of numbers that are multiple of 5 are", num5+num_both)
print("Count of numbers that are multiple of 3 & 5 both are", num_both)