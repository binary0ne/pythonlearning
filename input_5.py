number = input("Let me check, does your number" +
	"multiples by 10?\nPlease enter your number\n")
number = int(number)

if number % 10 == 0:
	print(str(number) + " is dividible by 10!")
else:
	print(str(number) + " is not dividible by 10!")