for x in range(1,21):
	print(x)

million = [x for x in range(1,1000001)]
print(min(million))
print(max(million))
print(sum(million))

odd = [x for x in range(2,21,2)]
for x in odd:
	print(x)

third = [x for x in range(3,31,3)]
for x in third:
	print(x)

cube = [x**3 for x in range(1,11)]
n = 1
for x in cube:
	print("Cube of " + str(n) + " is " + str(x))
	n +=1