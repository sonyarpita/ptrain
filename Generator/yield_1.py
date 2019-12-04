def print_odd(data):
	for x in data:
		if x %2==1:
			yield x
data=[1,4,5,6,7]
print("Odd numbers in list= ",end=" ")
for i in print_odd(data):
	print ("Sony",i, end=" ")
print("\n")
