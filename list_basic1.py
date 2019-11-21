u_list=[10,"Hai",7.5,1000]
#Forward Index
for i in range(len(u_list)):
	print("u_list[",i,"]:",u_list[i])

#Backward Index
for i in range(1,len(u_list)+1):
	print("u_list[",-i,"]:",u_list[-i])
u_list[1]=1000
print(u_list)
