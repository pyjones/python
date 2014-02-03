the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# Going through a list:
for number in the_count:
	print "This is count %d" % number

# and again
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# Going through mixed lists. Use of %r as not sure whether it's a number or string
for i in change:
	print "I got %r" % i

# Building lists
elements = []

# Using a range function to do 0 to 5 counts
for i in range(0, 6):
	print "adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)

# now print out the new list:
for i in elements:
	print "Element was: %d" % i

print range(5,10)
