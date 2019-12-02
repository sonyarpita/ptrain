class student:
	database="student"
	def get_details(self,aname,arno,afee):
		self.name=aname
		self.rno=arno
		self.fee=afee
	def put_details(self):
		print("Name= ",self.name)
		print("Roll No = ",self.rno)
		print("Fee = ", self.fee)
		print("Database =", self.database)
s1=student()
s2=student()
print("Object:1st created object details")
s1.get_details("john", 426, 5000.00)
s1.put_details()
print("database is",student.database)
print("Object:2nd Created object details")
s2.get_details("abraham",450,42000.00)
s2.put_details()
print("******************AFTER STUDENT DATABASE*****************")
s1.database="JOHN"
print("Object: 1st object details")
s1.put_details()
print("Object: 2nd object details")
s2.put_details()
