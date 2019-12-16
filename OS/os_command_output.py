import os
os.system("ps > redirect.txt")
f_obj=open("redirect.txt")
pid_list=[]
content=f_obj.readlines()
flag=False
for line in content:
	if flag:
		string=" ".join(line.split())
		#conv_list=line.split(" ")
		conv_list=string.split(" ")
		print(conv_list)
		pid_list.append(conv_list[0])
	flag=True
print(pid_list)
