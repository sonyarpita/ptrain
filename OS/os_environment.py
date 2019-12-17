import os
print(os.environ['HOME'])#/users/sony
print(os.environ.get('HOME'))#/users/sony

for k in os.environ.keys():
	print(k,":",end="")
	print(os.environ[k])
