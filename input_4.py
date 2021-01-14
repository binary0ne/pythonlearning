guests = input("How many people are in your dinning group?\n")
guests = int(guests)

if guests > 8:
	print("You should wait for a table.")
else:
	print("Your table is ready!")