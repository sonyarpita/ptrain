num_of_nums=int(input("Enter number of numbers to be sorted: "))
user_input_num_list=[]
simi=[]
def enter_list_elements(x):
	for i in range(x):
		i=int(input("Enter elements: "))
		user_input_num_list.append(i)
	return user_input_num_list

print("List=",enter_list_elements(num_of_nums))


def similar(user_input_num_list):
	for i in range(len(user_input_num_list)):
		for j in range(1,len(user_input_num_list)+1):
			if i!=len(user_input_num_list)-j and user_input_num_list[i]==user_input_num_list[-j]:
				simi.append(user_input_num_list[i])
	return simi


def largest(user_input_num_list):
	for i in range(len(user_input_num_list)):
		counter=0
		for j in range(1,len(user_input_num_list)+1):
			if user_input_num_list[-j]<=user_input_num_list[i] and i!=len(user_input_num_list)-j:
				counter=counter+1
			if counter==len(user_input_num_list)-1:
				return user_input_num_list[i]


def smallest(user_input_num_list):
	for i in range(len(user_input_num_list)):
		counter=0
		for j in range(1,len(user_input_num_list)+1):
			if user_input_num_list[-j]>=user_input_num_list[i] and i!=len(user_input_num_list)-j:
				counter=counter+1
			if counter==len(user_input_num_list)-1:
				return user_input_num_list[i]

print("Similar elements=",similar(user_input_num_list))
print("Largest element=",largest(user_input_num_list))
print("Smallest element=",smallest(user_input_num_list))


