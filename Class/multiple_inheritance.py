class g_Father():
	surName=""
	habbits=""
	attitude=""
	def __init__(self,surname,habbits,attitude):
		self.surName=surname
		self.habbits=habbits
		self.attitude=attitude
class Father():
	fname=""
	color=""
	skill=""
	def __init__(self,fname,color,skill):
		self.fname=fname
		self.color=color
		self.skill=skill
class son(g_Father,Father):
	name=""
	kind=""
	bold=""
	def __init__(self,surname,habbits,attitude,fname,color,skill,kind,bold):
		g_Father.__init__(self,surname,habbits,attitude)
		Father.__init__(self,fname,color,skill)
		self.name=self.surName+self.fname
		self.kind=kind
		self.bold=bold
	def display(self):
		print("Son Name: ",self.name)
		print("Son Kind: ",self.kind)
		print("Son Bold: ",self.bold)
		print("Son Habbits: ",self.habbits)
		print("Son Attitude: ",self.attitude)
		print("Son Color: ",self.color)
		print("Son Skills: ",self.skill)
s=son("Sandhti","cricket,reading","good","Raja Shekar","White","Talented","Honest","False")
s.display()
