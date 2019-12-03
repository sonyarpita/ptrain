class OwnIterator:
	def __init__(self,num=0):
		self.number=num
	def __iter__(self):
		self.x=1
		return self
	def __next__(self):
		if self.x<=self.number:
			own_iterator=self.x
			self.x+=1
			return own_iterator
		else:
			raise StopIteration
for x in OwnIterator(10):
	print("Num = ",x)
