class addOvrld:
	def __init__(self,a=0,b=0):
		self.a=a
		self.b=b
	def __str__(self):
		return "({0},{1})".format(self.a,self.b)
	def __add__(self,other):
		a=self.a+other.a
		b=self.b+other.b
		return addOvrld(a,b)
obj1=addOvrld(2,3)
obj2=addOvrld(2,2)
obj=addOvrld(2,3)
print("Addition of 3 Objects= ", obj1+obj2+obj)

