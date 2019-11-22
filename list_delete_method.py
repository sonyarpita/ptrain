or_list1=[1,2,3,4]
or_list2=[1.2,2.5,3.6,4.3]
print(or_list1)
print(or_list2)
del or_list1[0]
print(or_list1)
del or_list1[:]
print(or_list1)
del or_list2[0:1]
print(or_list2)
del or_list2[0:len(or_list2)]
print(or_list2)

