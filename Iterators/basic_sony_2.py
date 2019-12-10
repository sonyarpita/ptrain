class OwnIterator:
	def __init__(self,num):
	    self.number=num
	def __iter__(self):
            self.a=1
            print("Value of self.num=", self.a)
            return self
	def __next__(self):
		if self.a<=self.number:
			own_iterator=self.a
			self.a+=1
			return own_iterator
		else:
			raise StopIteration
for x in OwnIterator(10):
	print("Num = ",x)
