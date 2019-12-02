class student:
	def get_details(self):
		self.name="john"
		self.rno=429
		self.fee=50000.00
	def put_details(self):
		print("Name = ", self.name)
		print("Roll No = ", self.rno)
		print("Fee = ",self.fee)
obj=student()
obj.get_details()
obj.put_details()
