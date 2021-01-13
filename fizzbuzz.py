def fizzbuzz(x):
	array = ""
	if x % 3 == 0:
		array = "fizz"
	if x % 5 == 0:
		array += "buzz"
	if x % 3 != 0 and x % 5 != 0:
		print(x) 
		return(x)
	else:
		print(array)
		return(array)

for x in range(1,101):
	fizzbuzz(x)