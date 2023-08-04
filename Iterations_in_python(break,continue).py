l = [10,20,30,40,50]
key = 10

# for value in l:
#	if value == key:
#	    print("element found")
#	    break
#	else:
#	    continue
# else:
#	print("element not found")

for index, value in enumerate(l):
    # print(index, value)
    if value == key:
    	print("element found at index", index)
    	break
    else:
    	# continue
    	pass
    	print("this is the statement after the continue statement")
else:
	print("element not found")

## Note: Any statement after the continue statement is the un-reachable part of the code
## Note: Any statement after the pass statement is the always reachable part of the code
