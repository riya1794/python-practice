def print2(*args):
	a1, a2 = args;
	print a1,
	print a2

def printw2(a1,a2):
	print a1,
	print a2

def printret(a):
	b=a*10;
	c=a*100;
	return b,c

print2("a" , "b")
printw2("a" , "b")
a,b = printret(1)
print "val returned ", a,b