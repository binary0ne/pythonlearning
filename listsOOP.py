#Learning OOP
#Creating class
class invitelist():
	def __init__(self):
		self.list = []

#Defining functions		
#Invitation function
	def invite_ppl(self):
		for x in self.list:
			message = "Dear " + x.title() + ". I honorably invite you to a dinner. Today at 7pm on our place"
			print(message)

#Remove function, leaves only defined amount of firsts in list
	def remove_ppl(self, desired_amount):
		n = len(self.list)
		while n > desired_amount:
			excluded = self.list.pop()
			n -= 1
			message = "Sorry " + excluded.title() + ", but you are out!"
			print(message)

#Remove by name function
	def exclude_ppl(self, name):
		self.list.remove(name)
		message = "It is sorry to hear, " + name.title() + ", that you cant go with us."
		print(message)

#Wipe function
	def wipe_ppl(self):
		for x in reversed(self.list):
			self.list.remove(x)

#Populate function
	def add_ppl(self, list_toadd):
		for x in list_toadd:
			self.list.append(x)

#Setting list out
print("Invitation for these honorable people\n")
guests = invitelist()
guests.add_ppl(["albert einstein", "doctor watson", "mark cross"])

#Invitation cycle
guests.invite_ppl()

#Message to absent + removal
print("\nOne of us has fallen ill =(\n")
guests.exclude_ppl("doctor watson")

#Adding new and sending new invites
print("\nBut we have new one! Ave Caesar\n")
guests.add_ppl(["gaius julius caesar"])
guests.invite_ppl()

#Adding even more guests
print("\nStop, wait, even more guys!\n")
guests.add_ppl(["jesus", "monty python", "caiser wilghelm"])

#Printing this fantastic feast guys
guests.invite_ppl()

#Remove all but 2
print("\nOh, shi... not too many places\n")
guests.remove_ppl(2)

#Invite last 2 of them
print("\n...and reinviting last ones...\n")
guests.invite_ppl()

#Wiping list
guests.wipe_ppl()

#Checking list
print(guests.list)