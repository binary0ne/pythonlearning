#Make an empty list for storing aliens.
aliens = []

#Make 30 green aliens.
for alien_number in range(30):
	alien_name = "alien_" + str(alien_number)
	new_alien = {"name": alien_name, "color": "green", "points": 5, "speed": "slow"}
	aliens.append(new_alien)

#Make 3 yellow aliens.
for alien in aliens[0:3]:
	if alien["color"] == "green":
		alien["color"] = "yellow"
		alien["speed"] = "medium"
		alien["points"] = 10
	elif alien["color"] == "yellow":
		alien["color"] = "red"
		alien["speed"] = "fast"
		alien["points"] = 15

#Show the first 4 aliens.
for alien in aliens[:5]:
	print(alien)
print("...")

#Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))