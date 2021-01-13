favourite_languages = {
	"jen": "python",
	"sarah": "c",
	"edward": "ruby",
	"phil": "python",
	}

print("Sarah's favourite language is " + 
	favourite_languages["sarah"].title() +
	".")

for person in favourite_languages:
	print(person.title() + "'s favourite language is " + favourite_languages[person].title() + ".")

person = {
	"name": "pjotr",
	"last_name": "vishnevski",
	"age": 23,
	"city": "tallinn",
	}
print(person["name"].title() + " " + person["last_name"].title() + " of " + str(person["age"]) +
	" years old is living in " + person["city"].title() + ".")

