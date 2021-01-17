def make_shirt(size="l", label="I love Python!"):
	print("You have selected shirt with size " + size.title() + ", and printed '" +
		label + "' text on it.")

make_shirt("m", "Destroy")
make_shirt(label="Hello World", size="l")

make_shirt()
make_shirt("m")
make_shirt(label="Coder here!")


def describe_city(city, country="estonia"):
	print(city.title() + " is in " + country.title() + ".")

describe_city("tallinn")
describe_city("tartu")
describe_city("moscow", "russia")