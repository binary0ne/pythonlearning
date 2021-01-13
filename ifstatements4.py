alien_color = "red"
points = 0

if alien_color == "green":
	points = 5
elif alien_color == "yellow":
	points = 10
elif alien_color == "red":
	points = 15

print("You earned " + str(points) + " points!")

age = 100

if age < 2:
	age_name = "baby"
elif age < 4:
	age_name = "toddler"
elif age < 13:
	age_name = "kid"
elif age < 20:
	age_name = "teenager"
elif age < 65:
	age_name = "adult"
else:
	age_name = "elder"

print("You are a " + age_name + "!")

fruits = ["apple", "coconut", "pineapple"]

if "apple" in fruits:
	print("You really like apples!")
if "coconut" in fruits:
	print("You really like coconuts!")
if "pineapple" in fruits:
	print("You really like pineapples!")
if "banana" in fruits:
	print("You really like bananas!")
if "kiwi" in fruits:
	print("You really like kiwis!")