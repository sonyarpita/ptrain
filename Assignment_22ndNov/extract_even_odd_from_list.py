num_of_nums=int(input("Enter number of numbers to be sorted: "))
user_input_num_list=[]
even_list=[]
odd_list=[]

def enter_list_elements(x):
    for i in range(x):
        y=int(input("Enter elements: "))
        user_input_num_list.append(y)
    print(user_input_num_list)

enter_list_elements(num_of_nums)

def even(user_input_num_list):
    for i in range(len(user_input_num_list)):
        divi=user_input_num_list[i]%2
        if divi==0:    
            even_list.append(user_input_num_list[i])
    return even_list


def odd(user_input_num_list):
    for i in range(len(user_input_num_list)):
        divi=user_input_num_list[i]%2
        if divi!=0:    
            odd_list.append(user_input_num_list[i])
    return odd_list

       
print("Even Numbers in the entered List: ",even(user_input_num_list))
print("Odd Numbers in the entered List",odd(user_input_num_list))


