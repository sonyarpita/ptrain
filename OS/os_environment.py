import os
print(os.environ['HOME'])#/users/naveen
print(os.environ.get('HOME'))#/users/naveen

for k in os.environ.keys():
	print(k,":",end="")
	print(os.environ[k])
