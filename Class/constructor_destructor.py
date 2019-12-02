class student:
	def __init__(self,aname,arno,afee):
		self.name=aname
		self.rno=arno
		self.fee=afee
	def put_details(self):
		print("Name= ",self.name)
		print("Roll No = ",self.rno)
		print("Fee = ", self.fee)
	def __del__(self):
		print("Object destroyed")
s1=student("john", 426, 5000.0)
s2=student("abraham",450,42000.00)
print("Object:1st Created object details")
s1.put_details()
print("Object:2nd Created object details")
s2.put_details()
