cities = {
	"tallinn": {
		"population": 400000,
		"country": "estonia",
		"fact": "It is a seaside city",
	},
	"moscow": {
		"population": 16000000,
		"country": "russia",
		"fact": "Capital of Russia",
	},
	"riga": {
		"population": 600000,
		"country": "latvia",
		"fact": "Very old city",
	},
}

for city, information in cities.items():
	print(city.title())
	print(information["country"].title() + ", " +
		str(information["population"]) + " of people, " +
		information["fact"])