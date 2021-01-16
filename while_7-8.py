sandwich_orders = ["tuna", "salami", "beef", "cesar", "shrimps"]
finished_sandwiches = []

while sandwich_orders:
	sandwich = sandwich_orders.pop()

	print("Making " + sandwich + " sandwich...")

	finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
	print("We did a " + sandwich + " sandwich!")