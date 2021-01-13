users = ["john", "simon", "katarina", "admin", "larry"]

if users:
	for user in users:
		if user == "admin":
			print("Hello admin, do you want to get a status report")
		else:
			print("Hello " + user.title() + ", how are you today?")
else:
	print("No user recognized, please try again.")


new_users = ["JOHN", "Samanta", "TERRy", "Derek", "tomas"]
current_users = ["john", "terry", "mike"]

for user in new_users:
	if user.lower() in current_users:
		print("Sorry " + user + ", but this username is taken.")
	else:
		print("Username " + user + " is available!")

numbers = [number for number in range(0,10)]
for number in numbers:
	if number == 1:
		print(str(number) + "st")
	elif number == 2:
		print(str(number) + "nd")
	elif number == 3:
		print(str(number) + "rd")
	else:
		print(str(number) + "th")