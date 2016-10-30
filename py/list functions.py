list1 = [1,2,3]
list2 = [4,5,6]

print list1+list2      #[1,2,3,4,5,6]
print list1*3          #[1,2,3,1,2,3,1,2,3]
print 3 in list1       #True
print 3 in list2       #False

print "length of the list : "
print len(list1)

list3 = [1,2,3]
print "comparsion of the 2 list : "
print cmp(list1,list2) # -1 as list1 is smaller 
print cmp(list2,list1) # 1 as list2 is bigger
print cmp(list1,list3) # 0 as same

print max(list1)
print min(list1)

new_list = []

for i in range(6):
	new_list.append(i)

print new_list
new_list.append(3)
print "list after appending 3", new_list

print new_list.count(3)    #count number of 3 in the list
print new_list.index(2)
print new_list.pop(0)
print new_list.pop(-1)
new_list.remove(2)
print new_list
new_list.reverse()
print new_list

list4 = [2,3,2,31,1,0]
list4.sort()
print list4