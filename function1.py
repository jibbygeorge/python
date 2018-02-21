# This is a simple function:


def hello_world():
	''' This is a doc stream: call with help function name'''

	print "This is hello world"
	x = 100
	return x

def my_name(name):
	myname = name + (' George')
	return  myname
	



a = hello_world()
print a

if a == 100:
	print "its true"

else:
	print "not true: false"

name = my_name("Jibby")
print "My name is %s" %(name)

