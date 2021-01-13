#Defining functions
#Invitation function
def invite_ppl(list):
	for x in list:
		message = "Dear " + x.title() + ". I honorably invite you to a dinner. Today at 7pm on our place"
		print(message)

#Remove function, leaves only defined amount of firsts in list
def remove_ppl(list, amount):
	n = len(list)
	z = amount
	while n > z:
		excluded = list.pop()
		n -= 1
		message = "Sorry " + excluded.title() + ", but you are out!"
		print(message)

#Remove by name function
def exclude_ppl(list, name):
	removed_name = name
	list.remove(removed_name)
	message = "It is sorry to hear, " + removed_name.title() + ", that you cant go with us."
	print(message)

#Wipe function
def wipe_ppl(list):
	for x in reversed(list):
		list.remove(x)

#Setting list out
print("Invitation for these honorable people\n")
guests = ["albert einstein", "doctor watson", "mark cross"]

#Invitation cycle
invite_ppl(guests)

#Message to absent + removal
print("\nOne of us has fallen ill =(\n")
exclude_ppl(guests, "doctor watson")

#Adding new and sending new invites
print("\nBut we have new one! Ave Caesar\n")
guests.append("gaius julius caesar")
invite_ppl(guests)

#Adding even more guests
print("\nStop, wait, even more guys!\n")
guests.insert(0, "jesus")
guests.insert(2, "monty python")
guests.append("caiser wilghelm")

#Printing this fantastic feast guys
invite_ppl(guests)

#Remove all but 2
print("\nOh, shi... not too many places\n")
remove_ppl(guests, 2)

#Invite last 2 of them
print("\n...and reinviting last ones...\n")
invite_ppl(guests)

#Wiping list
wipe_ppl(guests)

#Checking list
print(guests)