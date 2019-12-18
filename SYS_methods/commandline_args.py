import sys
print(sys.argv) #list of the values
print(sys.argv[0]) #by default always first element is file name 
sume=0
length=len(sys.argv)
if(length>1):
	for i in range(1, len(sys.argv)):
		sume+=int(sys.argv[i])
if(sume!=0):
	print("Sum=",sume)
else:
	print("Invalid commandline arguments")
