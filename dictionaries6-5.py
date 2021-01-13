rivers = {
	"danube": "poland",
	"misissipi": "usa",
	"don": "russia",
	"pirita": "estonia",
	"gang": "india",
	"oder": "germany",
}

for river, country in rivers.items():

	if country == "usa":
		country = country.upper()
	else:
		country = country.title()

	print("In a nice country " +
		country + " flows a great river " +
		river.title() + " which has nice sunsets!")

print(rivers)
rivers["sena"] = "france"

for river, country in rivers.items():
	if country == "usa":
		country = country.upper()
	else:
		country = country.title()
	print("In a nice country " +
		country + " flows a great river " +
		river.title() + " which has nice sunsets!")

for river in rivers.keys():
	print("Such a beautifull river " + river.title() + "!")

for country in rivers.values():
	if country == "usa":
		country = country.upper()
	else:
		country = country.title()
	print("Proud country of " + country + "!")