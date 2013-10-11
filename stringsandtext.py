#Playing with strings and text 

x = "There are %d types of people." % 2
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

print x
print y

print "I said: %r" % x
print "I also said: '%s'." % y

hilarious = False
evaluation = "Isn't that joke so funny?! %r"

print evaluation % hilarious

w  = "this is the left side of..."
e = "a string with a right side."

f = 1
g = 2

print w + e

print f + g