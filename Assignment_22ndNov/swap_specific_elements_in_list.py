num_of_nums=int(input("Enter number of numbers to be sorted: "))
user_input_num_list=[]
def enter_list_elements(x):
    for i in range(x):
        y=int(input("Enter elements: "))
        user_input_num_list.append(y)
    return user_input_num_list

print("List before swap",enter_list_elements(num_of_nums))

def print_index_element_list(user_input_num_list):
    for i in range(len(user_input_num_list)):
        print("At index[",i,"]=",user_input_num_list[i])
    a=int(input("Enter first index: "))
    b=int(input("Enter second index: "))
    c=user_input_num_list[a]
    user_input_num_list[a]=user_input_num_list[b]
    user_input_num_list[b]=c
    return user_input_num_list

print("Enter index to swap",print_index_element_list(user_input_num_list))









