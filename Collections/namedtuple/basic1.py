from collections import namedtuple
Student=namedtuple('Student','fname,sname,age')
s=Student('Sony','Das','31')
print(s.fname)
print(s.sname)
print(s.age)
