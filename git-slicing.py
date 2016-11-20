
#Python strings
#--------------

#string is immutable

'''
Multiline comment
'''
text = "Hellow World!!"
print text

print text+"     \
Python"

print """Hellow
               world
                    python"""

print '''Hellow
               world
                    python'''

print text
print "Slicing of string \"{}\"".format(text)
print "Slicing of the string %s" % text

#Slicing ---------------------------------------

#we know first and last indices of the string array

if text == "Hellow World!!!": print "yahoo! match found"
elif text > "I am a programmer ": print "Yahoo programmer line ,match found"
else:print "No string manipulation"


# Python doesn't have C style ! || && but python is using and or not


speed = 20
if speed >= 20 and text == "Hellow World!!":
    print "'and' operation in python"


# python