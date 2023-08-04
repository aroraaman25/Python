# 1) INT: to store the values that does not contain any decimal 
#num1 = 10
#print(type(num1))


# 2) Float: to store the values with decimal
#num2 = 20.5
#print(type(num2))

# Note: "Integer" , "Float" & "String" are Immutable Data-Types
# Immutable Data-Types :- the datatypes for which the values cannot be changed for the same memory location


# 3) String: Anything that is defined in '', " ", or in "'  '" are said to be valid python string
#s = "Aman"
#print(s, type(s))
#s = "'Python' is string"
#print(s)


# 4) List: Anyhting that is enclosed in [] is list. Used to add multiple values.
#l = [5,10,15,20, "aman", "sonu"]
#print(l, id(l))
#l.append(30)
#print(l, id(l), type(l))

# Note:- Python List is Heterogeneous, i.e. it can store different types of data in it
# Note:- List is a Mutable datatype.
# which means i.e. Python will provide a way to Add, Update or Delete any elements in this list from the same memory location


# 5) Tuple: 
#t = (10, 20, 30)
#print(t, type(t))

#Note:- Tuple is also an Immutable datatype just like int, float & string


# 6) Dictionary: A datatype in which elements are stored in Key-Value Pairs also called as Hash-Maps.
#d = { "name": "aman", "email":"abc@gmail.com"}
#print(d, type(d))

# Note:- Dict is a Mutable Datatype just like "List"


# 7) Sets: 
#s = {10, 20, 30, 40}
#print(s, type(s))

# Note:- Set is also Mutable Datatype just like "List" & "Dictionary"


# 8) Boolean: 
#bool : True False


# 9) complex:
c = 4 + 3j
print(c, type(c))