proceed = "y"

while proceed == "y":

	number = input("Enter a number and I will tell you is it even or odd: ")
	number = int(number)

	if number % 2 == 0:
		print("\nThe number " + str(number) + " is even.")
	else:
		print("\nThe number " + str(number) + " is odd.")

	proceed = input("Do you want to check another number? [y/n]")

print("Thank you, and have a good day!")