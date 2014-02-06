from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"

	next = raw_input(">>> ")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")

def bear_room():
	print "there is a bear here"
	print "the bear has a pot of honey."
	print "the fat bear is in front of another door"
	print "how are you going to move the bear?"
	bear_moved = False

	while True:
		next = raw_input(">>> ")

		if next == "take honey": # If 'take honey' is entered and value is false, as it's originally set to. 
			print "bear moved value= %r" % bear_moved
			dead("The bear looks at you and then slaps your face")
		# BELOW ELIF is effectively saying AND NOT False which is therefore True but it doesn't re-assign bear_moved value. It needs to be true to go to this loop because the while loop is true
		elif next == "taunt bear" and not bear_moved: 
			print "bear moved value= %r" % bear_moved # Still false, as it's not been reassigned
			print "The bear has moved from the door. You can go through"
			bear_moved = True # This is reassignment
		elif next == "taunt bear" and bear_moved: # If the value is True it goes to this condition
			print "bear moved value= %r" % bear_moved
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved: # If the value is true it goes to this condition
			print "bear moved value= %r" % bear_moved
			gold_room()
		else:
			print "I got no idea what that means."

def dimple_room():
	print "Here you see the great evil Simon"
	print "She stares at you and you go insane"
	print "Do you flee for your life or eat your head?"

	next = raw_input(">>> ")

	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		dimple_room()

def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"

	next = raw_input(">>> ")

	if next == "left":
		bear_room()
	elif next == "right":
		dimple_room()
	else:
		dead("Well that was rather silly, as you didn't input right or left. You're going to starve")

start()