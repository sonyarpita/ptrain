num_of_nums=int(input("Enter number of numbers to be sorted: "))
user_input_num_list=[]

def enter_list_elements(x):
    for i in range(x):
        i=int(input("Enter elements: "))
        user_input_num_list.append(i)
        return user_input_num_list

enter_list_elements(num_of_nums)
print("Largest Number=",max(user_input_num_list))
print("Smallest Number=",min(user_input_num_list))
print(user_input_num_list.index(2,2)) 

'''def equal_elements(user_input_num_list):
    length_of=len(user_input_num_list)
    print("Number of elements=",length_of)
    for i in range(len(user_input_num_list)):
        #length_of=0
        for j in range(1,len(user_input_num_list)+1):
           if user_input_num_list[i]==user_input_num_list[-j]:
                print("Similar elements=",user_input_num_list[i])
                length_of=length_of-1
                #print("Similar element=",user_input_num_list[i])
    return length_of
'''
'''def largest(user_input_num_list):
    length_of=equal_elements(user_input_num_list)
    print("Number of unequal elements=",length_of)
    #for i in range(len(user_input_num_list)):
    for i in range(length_of):
        counter=0
        for j in range(1,length_of+1):
            #print(user_input_num_list[i],user_input_num_list[-j])
            if user_input_num_list[i] > user_input_num_list[-j]:
                counter=counter+1
                #print("For",user_input_num_list[i],"Counter=",counter)
        if counter==length_of-1:
            #print("Inside Loop",user_input_num_list[i])
            return user_input_num_list[i]

def smallest(user_input_num_list):
    length_of=equal_elements(user_input_num_list)
    #for i in range(len(user_input_num_list)):
    for i in range(length_of):
        counter=0
        #for j in range(1,len(user_input_num_list)+1):
        for j in range(1,length_of+1):
            #print(user_input_num_list[i],user_input_num_list[-j])
            if user_input_num_list[i] < user_input_num_list[-j]:
                counter=counter+1
        #       if counter==len(user_input_num_list)-1:
        if counter==length_of-1:
            return user_input_num_list[i]
#equal_elements(user_input_num_list)
print("Largest Number=",largest(user_input_num_list))
print("Smallest Number=",smallest(user_input_num_list))'''
#print("Equal Elements=",equal_elements(user_input_num_list))


