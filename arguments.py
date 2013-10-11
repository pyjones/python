#Playing with arguments

from sys import argv

user = argv
prompt = '>>>'

print "Hi %s" % (user)
print "I'd like to ask you a few questions..."
print "First, do you like me %s?" % (user)
do_you_like_me = raw_input(prompt)

print "Second, where do you live?"
lives = raw_input(prompt)

print "Are you an Apple or Windows?"
computer = raw_input(prompt)

print """
Ok, so you said %r about whether you like me or not.
You live in %r. Great!
And you are a %r computer user. Ok!
""" % (do_you_like_me, lives, computer)