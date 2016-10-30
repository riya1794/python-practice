class person(object):
	def __init__(self, eyes, nose):
		self.eyes=eyes
		self.nose=nose

	def talk(self):
		print "person can talk"

class student(object):
	def __init__(self, name, rollno):
		self.name=name;
		self.rollno=rollno

	def mark(self, m):
		print "%s has marks %d " %(self.name , m)

	def talk(self):
		print "student can talk"

class mary(student, person):
	def __init__(self, name, rollno, sub , marks):
		#super(mary, self).__init__("Mary", 12115070)
		self.sub=sub;
		self.marks=marks

	def printf(self):
		print "My name is %s, my rollno is %d" %(self.name, self.rollno)
		print "I have %d subjects in which my scores are" %self.sub
		i=1
		for m in self.marks:
			print "%d subject: %d" %(i,m)
			i+=1

# not necesary to initialise any class, it always calls student talk()
mary = mary("Mary", 12115070, 5 , [10,20,30,40,50]
mary.talk()

student("Ram", 12115060).mark(40)
