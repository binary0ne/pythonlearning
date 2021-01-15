#Very bad and complex solution, however, for educational purposes

prompt = "\nHello, dear customer, you can write toppings you want"
prompt += " us to add to your pizza. To finalize the order write 'quit'\n"

print(prompt)
toppings = []
topping = ""
addtopping = ""
while addtopping != "quit":
	addtopping = input()
	if addtopping == "quit":
		for topping in toppings:
			if "displaytopping" in locals():
				displaytopping += ", " + topping.title()
			else:
				displaytopping = topping.title()
		print("We will make a pizza with " + displaytopping + " for you!")
	else:
		toppings.append(addtopping)