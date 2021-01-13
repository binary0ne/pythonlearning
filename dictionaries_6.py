favourite_languages = {
	"jen": "python",
	"sarah": "c",
	"edward": "ruby",
	"phil": "python",
	}

for name, language in favourite_languages.items():
	print(name.title() + "'s favourite language is " +
		language.title() + ".")

for name in favourite_languages.keys():
	print(name.title())

friends = ["phil", "sarah"]
for name in favourite_languages.keys():
	print(name.title())

	if name in friends:
		print(" Hi " + name.title() +
			", I see your favourite language is " +
			favourite_languages[name].title() + "!")

if "erin" not in favourite_languages.keys():
	print("Erin. please take our poll!")