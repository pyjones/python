#Reading and writing to files

from sys import argv

script, filename = argv

print "Let's erase %r" % filename
print "If you don't want to do that, hit Ctrl-C."
print "If you're ok with that, hit return."

raw_input ("?")

print "Opening the file... (%r)" % filename
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now, let's write to a new file, 3 lines worth"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "Thanks. Now I'll save those lines"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "Now I'll close the file"
target.close()
