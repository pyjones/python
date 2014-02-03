def increment(maximum):
	num = 0
	while num < maximum:
		print "At the top of the list we have %d" % num
		listincrement.append(num)

		num = num + 1
		print "numbers now: ", listincrement
		print "At the bottom the number is %d" % num


prompt = ">>>"
listincrement = []


print "input a number to count up to: "
max_num = int(raw_input(prompt))

print "This is the while loop: %r " % increment(max_num)


