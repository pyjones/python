def spaces_spare(cars, people, space):
	cars * space = total_space
	total_space / cars = spare_spaces
	return spare_spaces


prompt = ">>>"
space_in_car = 5

### SCRIPT STARTS HERE

print "Number of people travelling to Congress"

ppl_to_congress = raw_input(prompt)

print "Number of cars"

cars_to_congress = raw_input(prompt)

spare_spaces = spaces_spare(cars_to_congress, ppl_to_congress, space_in_car)

if space_in_car / ppl_to_congress > space_in_car * cars_to_congress:
	print "There are not enough cars going"
else:
	print "There are enough cars with %d spaces spare" % spaces_spare

