class person:
	name=""
	age=0
	def __init__(self,personName,personAge):
		self.name=personName
		self.age=personAge
	def display(self):
		print("Name= ", self.name)
		print("Age= ", self.age)
	def __del__(self):
		print("object destroyed")
class student(person):
	studentid=""
	fee=0.0
	def __init__(self,studentName,studentAge, studentid,fee):
		person.__init__(self,studentName,studentAge)
		self.studentid=studentid
		self.fees=fee
	def getId(self):
		return self.studentid
	def getFee(self):
		return self.fee
	def __del__(self):
		print("Obecjt destroyed")
print("Person details are")
print("***********************")
person1=person("Ricky",50)
person1.display()
print("***********************")
print("Student details are")
print("***********************")
student1=student("Sony", 50, "129", 500000)
student1.display()
print("Student Id: ", student1.getId())
print("Student Fee: ",student1.getFee())
print("*********************************")
