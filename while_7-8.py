sandwich_orders = ["pastrami", "tuna", "salami", "pastrami", "beef", "pastrami", "cesar", "shrimps"]
finished_sandwiches = []

print("We are out of pastrami")
while "pastrami" in sandwich_orders:
	sandwich_orders.remove("pastrami")

while sandwich_orders:
	sandwich = sandwich_orders.pop()

	print("Making " + sandwich + " sandwich...")

	finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
	print("We did a " + sandwich + " sandwich!")