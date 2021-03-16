class TestClass():
	def __init__(self, name):
		self.name = name

	def hello(self):
		print("Hello, I am a " + self.name)


dictionary = {"a": "dog", "b": "cat", "c": "parrot"}

for key, value in dictionary.items():
	dictionary[key] = TestClass(value)

for key in dictionary.keys():
	dictionary[key].hello()