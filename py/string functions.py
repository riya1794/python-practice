import string

str = "check string functions"

print "first check sort function working  :  "
print sorted(str)            #sort is characcter wise sort

print "here is the split funtion : "
print str.split(' ')

print "single character printing : "
print str[0]

print "print substring of string : "
print str[1:5]

num1 = "4"
num2 = "2"
print "convert string into long : "
a = string.atol(num1)
b = string.atol(num2)
print a+b

check = "how is ur repeat ur superb"
print "count occurance of an substring in an string : "
print check.count("ur")

print "find occurance of an substring in an string : "
print check.find("ur")
print check.find("not there")

print "alternate of find is index : genearate expetation when it is not found"
print check.index("ur")    #7 whereas in find it returned 2
#print check.index("not there") cannot check this

print "length of string : "
print len(str)

print "convert string into lower case"
print str.lower()

print "max and min occur character into string"
print min(str)
print max(str)

print "if we want to remove some character from string : "
print str.strip('s')

print "convert string into uppercase"
print str.upper()