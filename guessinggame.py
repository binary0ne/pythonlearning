import random

prompt = "What is your name?\n"

name = input(prompt)
print("Hello, " + name.title() + "!")
print("Lets play guessing game!")

guessed_number = random.randrange(1, 101)
print("I have minded a number from 1 to 100, lets try to guess it!")
attempts = 0
answer = 105

while answer != guessed_number:
	attempts += 1
	answer = input()
	answer = int(answer)
	if answer > guessed_number:
		print("Sorry, " + name.title() + ", I have minded a smaller number")
	elif answer < guessed_number:
		print("Sorry, " + name.title() + ", I have minded a bigger number")
	else:
		print("Exactly! " + name.title() + " you have guessed it right! This is " +
			str(guessed_number) + "! You spent " + str(attempts) 
			+ " attempts!")