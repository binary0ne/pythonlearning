#My fizzbazz solution

def fizzbuzz(x):
	if x % 15 == 0:
		return("fizzbuzz")
	elif x % 3 == 0:
		return("fizz")
	elif x % 5 == 0:
		return("buzz")
	else:
		return(x)



if fizzbuzz(15) == "fizzbuzz":
	print("Test1 passed")
else:
	print("Test1 failed")

if fizzbuzz(5) == "buzz":
	print("Test2 passed")
else:
	print("Test2 failed")

if fizzbuzz(3) == "fizz":
	print("Test3 passed")
else:
	print("Test3 failed")


test4array = ""
for x in range(1,31):
	test4array += str(fizzbuzz(x))
if test4array.count("fizz") == 10:
	print("Test4 passed")
else:
	print("Test4 failed") 

test5array = ""
for x in range(1,31):
	test5array += str(fizzbuzz(x))
if test5array.count("buzz") == 6:
	print("Test5 passed")
else:
	print("Test5 failed") 

if fizzbuzz(22) == 22:
	print("Test6 passed")
else:
	print("Test6 failed")