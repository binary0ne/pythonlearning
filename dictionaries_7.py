favourite_languages = {
	"jen": "python",
	"sarah": "c",
	"edward": "ruby",
	"phil": "python",
	}

for name in sorted(favourite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")

print("\nThe following languages have been mentioned:")
for language in set(favourite_languages.values()):
	print(language.title())

languages_statistics = {}
for language in favourite_languages.values():
	if language in languages_statistics:
		languages_statistics[language] += 1
	else:
		languages_statistics[language] = 1

print("\nPoll statistics:")
for key, value in languages_statistics.items():
	print(key.title() + " : " + str(value))

print(languages_statistics)

poll_candidates = ["jen", "sarah", "edward", "phil", "tomas", "andy", "george"]

for candidate in poll_candidates:
	if candidate in favourite_languages:
		print("Thank you, " + candidate.title() + " for your answer. " +
			"You have selected " + favourite_languages[candidate].title() +
			" as your favourite language!")
	else:
		print(candidate.title() + ", you should take the poll!")