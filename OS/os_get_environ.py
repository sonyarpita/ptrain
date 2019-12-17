import os 
print(os.environ["HOME"])
print(os.environ.get("HOME"))
for k in os.environ.keys():
	print(k, ":",end="")
	print(os.environ[k])
