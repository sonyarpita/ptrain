try:
	v1=int(input("Enter first number: "))
	v2=int(input("Enter first number: "))
	result=v1/v2
	print("Result is: ", result)

except ValueError:
	print("ValueError:Exception Handler")
	print("Invalid input: Only integers are allowed")
except ZeroDivisionError:
	print("ZeroDivisionError: Exception Handler")
	print("Oh!! divide by 0")
except IndentationError:
	print("IndentationError: Exception Handler")
finally:#this segment will be executed no matter what
	print("After executing finally")
