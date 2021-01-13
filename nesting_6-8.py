bobik = {
	"specie": "dog",
	"owner": "tomas",
}

kesha = {
	"specie": "parrot",
	"owner": "peter",
}

marusya = {
	"specie": "cat",
	"owner": "evelin",
}

gesha = {
	"specie": "python",
	"owner": "sandra",
}

pets = [bobik, kesha, marusya, gesha]

for pet in pets:
	print(pet["owner"].title() + " has a " + pet["specie"])