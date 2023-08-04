# Lists in Python
# 1) List is a Mutable Data-Type, i.e. various operations like add, subtract can be done with the elements
# 2) List is an Ordered Data-Structure i.e. it supports indexing and slicing
# 3) Heterogenous Data-Type: Any type of data can be stored in a List
# List just stores the reference of the values

# l=[10,20,30,40,"Python","Java","m#k%T&",["sonu","mota",100,200]]
# print(l, type(l))

# indexing & slicing in lists
# print(l[0],l[-1][0])
# print(l[:5],l[3:])

# l = [100,200,300,400,500,600]
# print(id(l))
#for value in l:
	#print(value)
# for value in l[::2]:
	# print(value)
# num1=100
# print(id(num1))

# Different methods to add elements in List
### 1) Append: to add a single element at a time
# l.append(700)
# l.append("Python")
# l.append([95,105,115])
# print(l)
#print(id(l[0]))

### 2) Extend: to add multiple elements at a time. This iterates over the list and treat each element as individual element
# l.extend([10,20,30,40,50])
# print(l)
# l.extend("Python")
# print(l)

## Note: Append & Extend will add the elements in the last of the given list

### Insert: To add the elements in the middle of the list. Only 1 element can be added at a time

# l.insert(5,"Aman")
# print(l)

l=[10,20,30]
l2=l.copy()
l.append(40)
#print(l,l2)
#print(id(l),id(l2))
