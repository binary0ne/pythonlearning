print("Write down age of your cinema party.\n" +
	"When finished, write 'quit'.")

total_price = 0
while True:
	age = input()

	if age == "quit":
		break
	else:
		age = int(age)

		if age < 3:
			total_price += 0

		elif age < 12:
			total_price += 10

		else:
			total_price += 15

print("Total price for your tickets would be " + str(total_price) +
	"$ accordingly!")