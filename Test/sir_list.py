import os
os.system("ps > redirect.txt")
f_obj=open("redirect.txt")
pid_list=[]
content=f_obj.readlines()
flag=False
for line in content:
    if flag: #taking the flag to skip the first entry, bcz name of the fields
        string=''.join(line.split())#Creating as a string with single space everyword
        conv_list=string.split(' ')#converting the string to a list
        print(conv_list)#individual list
        pid_list.append(conv_list[0])#adding all PID to list
    flag=True
print(pid_list)
