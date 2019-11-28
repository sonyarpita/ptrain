f=open("sony.txt","r")
for i in f.readlines():
    print(i)
f.close()
print("State: ",f.closed)
print("Name: ",f.name)
print("Mode",f.mode)

