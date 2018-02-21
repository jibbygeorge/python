#python Conditional Stetement:

x,y = 10, 100

st = "x is less than y" if (x < y) else "x is greater than or equal to y"
print st

#define a function
def func1():
	print "I am a function"

func1()

#function that takes argument
def func2(arg1, arg2):
	print arg1, " ", arg2

func2(10,20)

#Loops

def main():
	x = 0
	#define a while loop , while condition inside the parenthesis are true
	while (x < 5):
		print x
		x = x + 1
main()

#define a for loop , range is a function

for x in range(5,10):
	print x

#use for loop over a collection

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
for d in days:
	print d

#use break and continue statement
for x in range(5,10):
	if (x == 7): break # this will break the function when the condition is met
	if (x % 2 == 0): continue # when condition is met, it will continue to the beginning of the statement, it didnt print the below line

	print x

#Classes in python














