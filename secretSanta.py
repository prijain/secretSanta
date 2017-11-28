from twilio.rest import Client
import random

account_sid = "AC0220e11df6beadfe315afd84fdd6fa81"
auth_token = "043b15a020f47cce20f09af7246855c8"
twilioPhoneNumber = "+15204418736"

client = Client(account_sid, auth_token)


class Person:
	def __init__(self, name, phone):
		self.name = name
		self.phone = "+1" + str(phone) # Because twilio needs the "+1" US prefix to send messages

	def __str__(self):
		return self.name + ": " + str(self.phone)

	# gdi victor is this really better?
	def __eq__(self, other):
		return self.name == other.name and self.phone == other.phone

	# this is victor's fault
	def __hash__(self):
		return id(self)


def init():
	david = Person("David", "5208184387")
	victor = Person("Victor", "9135688428")
	pri = Person("Priyanka", "8324537544")
	iris = Person("Iris", "8058953373")
	lucy = Person("Lucy", "6508338839")
	alex = Person("Alex", "2818656710")

	return [david, victor, pri, iris, lucy, alex]

def shuffle():

	santas = init()
	options = init()
	pairings = {}

	for santa in santas:
		# A "santaee" is to "santa" as "employee" is to "employer"
		santaee = random.choice(options)
		# Don't be your own santa. Redraw until it's not.
		while santaee == santa:
			santaee = random.choice(options)
		
		pairings[santa] = santaee
		options.remove(santaee)

	for key, value in pairings.iteritems():
		# print str(key) + "\t|\t" + str(value)

		send(key, value)





def send(santa, santaee):
	bodyString = "Hi " + santa.name + ", your santaee is " + santaee.name + ". Don't fuck up."
	# message = client.messages.create(
	#     to=santa.phone, 
	#     from_=twilioPhoneNumber,
	#     body=bodyString)

	print bodyString

shuffle()
