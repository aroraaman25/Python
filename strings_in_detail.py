# string: is an im-mutable datatype, i.e. once defined the values cannot be changed in a particular memory location
# string: is an ordered data structure, i.e. python will maintain the same order structure in which the user will define a string
# string supports indexing as well as slicing


# s= "Python"
# print(id(s), type(s))

# s= "java"
# print(id(s), type(s))

# s= "Python is string" 
# print(s[0], s[-1])       #----- this is known as indexing

# print(s[0:6])       #---------- this is known as slicing
# print(s[:6])        #---------- this will print the value till 6th string

# print(s[7:])     #---- this will print the value after the 7th string

# print(s[::])     #---- this will print the entire thing between the ""

# print(s[::2])    #---- this will print the string by skipping 1 value at a time

# print(s[::-1])   #---- this will give the same string but in complete reverse order

# for value in s[::2]:
	# print(value)

# print(dir(str))

# 1) Format:
num1 = 100
num2 = 200
# print("value of num1 is", num1, "value of num2 is", num2)
# print("value of num1 is {val2} & value of num2 is {val1}".format(val1=num1, val2=num2))

s="aman arora"
# print(id(s))
# s = s.capitalize()
# print(s)
# print(id(s))

print(s.upper())
print(s.lower())
print(s.title())       ## ----------- converts the 1st character in Capital Letter
#print(s.islower())
