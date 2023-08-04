# Syntax in Python:

#if [condition]:
#	statements
#elif[condition]:
#	statements
#else:
#	statements

# Question: Compare the two variables

num1 = 100
num2 = 50

# rough work:
# 1- either num1 is greater
# 2- either num2 is greater
# 3- either num1 & num2 are equal

if num1 > num2:
	print("num1 is greater than num2")
elif num1 < num2:
	print("num2 is greater than num1")
else:
	print("both are equal")

