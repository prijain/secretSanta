from twilio.rest import Client
import random
import sys

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

def initPeople():
	david = Person("David", "5208184387")
	victor = Person("Victor", "9135688428")
	pri = Person("Priyanka", "8324537544")
	iris = Person("Iris", "8058953373")
	lucy = Person("Lucy", "6508338839")
	alex = Person("Alex", "2818656710")

	return [david, victor, pri, iris, lucy, alex]

def shuffle(useTwilio):
	santas = initPeople()
	options = initPeople()
	pairings = {}

	for santa in santas:
		# A "santaee" is to "santa" as "employee" is to "employer"
		santaee = random.choice(options)
		# Don't be your own santa. Redraw until it's not.
		while santaee == santa:
			santaee = random.choice(options)
		
		pairings[santa] = santaee
		options.remove(santaee)

	# Save an answer key, just in case
	masterKey = open("Secret Santa Master Key.txt", "w")
	if not useTwilio:
		print "\n"
		print "Welcome to Secret Santa"

	for key, value in pairings.iteritems():
		masterKey.write(str(key.name) + " is the santa of " + str(value.name) + ".\n")
		send(key, value, useTwilio)

	if not useTwilio:
		print "\n"

	masterKey.close()



def send(santa, santaee, useTwilio):
	bodyString = "Hi " + santa.name + ", your santaee is " + santaee.name + ". Don't fuck up."
	if useTwilio:
		message = client.messages.create(
		    to=santa.phone, 
		    from_=twilioPhoneNumber,
		    body=bodyString)
	else:
		print "\t" + bodyString

def main(useTwilio):
	shuffle(useTwilio)

if __name__ == '__main__':
    
    if len(sys.argv) == 1:
    	main(False)
    else:
	    flagArg = sys.argv[1]

	    if flagArg == "-h":
		    print "These are the help commands."
		    print "Use -t to send with twilio, -p to print locally."
	    elif flagArg == "-t":
	    	main(True)
	    elif flagArg == "-p":
	    	main(False)
	    else:
	    	main(False)
