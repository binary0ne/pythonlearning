#Store information about a pizza being ordered
pizza = {
	"crust": "thick",
	"toppings": ["mushrooms", "extra cheese"],
}

#Summarize the order
print("You ordered a " + pizza["crust"] + "-crust pizza " +
	"with the following toppings:")

for topping in pizza["toppings"]:
	print("\t" + topping.title())

favourite_languages = {
	"jen": ["python", "ruby"],
	"sarah": ["c"],
	"edward": ["ruby", "go"],
	"phil": ["python", "haskell"],
}

for name, languages in favourite_languages.items():
	print("\n" + name.title() + "'s favourite langauges are:")
	for language in languages:
		print("\t" + language.title())