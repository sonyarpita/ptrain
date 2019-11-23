'''
def funcn(a=10,b=20,c=30): Right
def funcn(a,b=20,c=30): Right
def funcn(a,b,c=30): Right
def funcn(a=10,b,c=30): Wrong
def funcn(a=10,b=20,c): Wrong
def funcn(a,b=20,c): Wrong
'''

def default_arg_fun(a=10,b=20,c=30):
	print("a=",a)	
	print("b=",b)	
	print("c=",c)
x=1
y=2
z=3
print("no arguments")
default_arg_fun()
print("1 argument")
default_arg_fun(x)
print("2 arguments")
default_arg_fun(x,y)
print("2 arguments")
default_arg_fun(x,z)
print("3 arguments")
default_arg_fun(x,y,z)	
