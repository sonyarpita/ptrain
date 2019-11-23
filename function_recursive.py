def calc_factorial(x):
	"""This is  recursive function
	to find the factorial of an integer"""
#	return(x*calc_factorial(x-1))
	if x == 1:
		return 1
	else:
		return (x*calc_factorial(x-1))

num=5
fact=calc_factorial(num)
print("Factorial of",num,"=",fact)

	
