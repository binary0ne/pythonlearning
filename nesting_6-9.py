favourite_places = {
	"sarah": ["paris", "milan", "cologne"],
	"tom": ["sweden", "tibet", "arctic"],
	"jeremy": ["kuba", "san-francisko", "miami"]
}

for person, places in favourite_places.items():
	print("\n" + person.title() + "'s favourite places are: ")
	for place in places:
		print("\t" + place.title())