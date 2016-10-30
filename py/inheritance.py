class first(object):
	#def __init__(self):
		#print "first "
	pass  # its is for empty blocks

class second(object):
	def __init__(self):
		print "second "

class third(object):
	def __init__(self):
		print "third "

class forth(first , second, third):
	def __init__(self):
		super(forth, self).__init__()
		print "forth "

a= forth()

# if first has __init__() function then call that n exits
#if not present then calls the __init__() function for second, if their then calls n exits
# if similarly for third
#if none then also no error
