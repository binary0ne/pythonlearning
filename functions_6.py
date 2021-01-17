def make_pizza(**toppings):
	print(toppings)
	for topping in toppings.values():
		print("- " + topping)

make_pizza(a='pepperoni')
make_pizza(a='pepperoni', b='cheese', c='jalapeno')