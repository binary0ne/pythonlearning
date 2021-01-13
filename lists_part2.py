my_foods = ["pizza", "falafel", "carrot cake", "wasabi", "sushi"]
friend_foods = my_foods[:]

my_foods.append("canoli")
friend_foods.append("ice cream")

print("My favourite foods are:")
print(my_foods)

print("\nMy frined's favourite foods are:")
print(friend_foods)

print(my_foods[:3])

delim = len(my_foods)
half = int(-(delim/2))
print(my_foods[half:])

print(my_foods[-3:])

my_pizzas = ["margarita", "pepperoni"]
friend_pizzas = my_pizzas[:]

my_pizzas.append("sea")
friend_pizzas.append("carbonara")

print("My favourite pizzas")
for pizza in my_pizzas:
	print("I like " + pizza.title())

print("My friends favourite pizzas")
for pizza in friend_pizzas:
	print("He likes " + pizza.title())