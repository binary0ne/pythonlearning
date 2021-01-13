requested_toppings = ["mushrooms", "green pepper", "extra cheese"]

for requested_topping in requested_toppings:
	if requested_topping == "green pepper":
		print("Soryy, we are out of green pepper right now")
	else:
		print("Adding " + requested_topping +".")

print("\nFinished making your pizza!")