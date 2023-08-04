## Splits & Joins

# Split ---------- if we want to convert string to list
# s = "Python/JAVA/HTML/CSS"
# l = s.split("/")
#print(l)

# Join ---------- if we want to convert the list back to string, join function can be used
# Join func. is exactly opposite of split func.

# s0 = (" ").join(l)
#print(s0)


## Maketrans & Translate
# s1="abcd"
# s2="1234"
# s3= "Aman is a boy abcd"
# table = str.maketrans(s1,s2)	
# result = s3.translate(table)
# print(result)


# "index, find & rfind" function in python

# s="HTML,CSS,PYTHON,PYTHON,PYTHON"
# now if i have to check whether PYTHON is present in the string or not then :
# print("PYTHON" in s)
# now if i have to find the index of the string PYTHON in the entire string, then:
# print(s.index("PYTHON"))

# print(s.find("python")) 

# print(s.rfind("PYTHON")) #---- similar to find func, but the only diff is that it will search the string from the right side

# the only difference b/w index & find/rfind func is that index func returns an error if something that is not present in the string 
# is searched using the index func whereas find/rfind func gives return as -1 in the same case


# strip, center, ljust, rjust, replace

# s="***This is a sample string***"
# print(s)
# s=s.strip("*")
# print(s)

# s0="aman"
# s1=s0.center(10,"*")
# print(s1)
# s2=s0.ljust(10,"*")
# print(s2)

s="html, css, python, java, ruby, pearl, bash"
s1=s.replace("css","linux")
print(s1)
