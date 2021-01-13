friends = ["petya", "andrei", "irina", "anton", "pasha", "nikita"]
n = 0

for friend in friends:
	message = "Good day " + friends[n].title() + "."
	print(message)
	n += 1