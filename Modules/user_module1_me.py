import swap
try:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    a,b=swap.swape(a,b)
    print("values after swap= ",a,",",b)
except ValueError:
    print("ValueError:Exception Handler")
    print("Invalid input: Only integers are allowed")
finally:
    print("Swapped")

