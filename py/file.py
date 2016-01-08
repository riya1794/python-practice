#file operation
from sys import argv

script , filename = argv

fs = open(filename)

str = fs.read(12)
print str;
print "file name is: " , fs.name
print "is file  closed: ", fs.closed
print "file mode: ", fs.mode
print "softspace: " , fs.softspace

print "currrent file pointer " , fs.tell()
print "sekked at 2"

fs.seek(2,0)

str = fs.read(10)
print str;

fs.close()