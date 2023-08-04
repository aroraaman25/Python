# Print numbers divisible by 5 & 7, between 1500 & 2700, both included

import os
os.system("cls")

count=0
for value in range(1500,2701):
	if (value%5) & (value%7) == 0:
		# print(value)
		count=count+1
print("count of divisible numbers is", count)