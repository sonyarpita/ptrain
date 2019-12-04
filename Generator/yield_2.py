def SquareNums():
	x=1
	while True:
		print ("Value of x= ",x)
		yield x*x
		x+=1

for num in SquareNums():
	if num>32:
		break
	print("Num is", num)

