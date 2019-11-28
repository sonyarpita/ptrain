num_of_nums=int(input("Enter number of numbers to be sorted: "))
user_input_num_list=[]
simi=[]
def enter_list_elements(x):
        for i in range(x):
                i=int(input("Enter elements: "))
                user_input_num_list.append(i)
        return user_input_num_list

print("List: ",enter_list_elements(num_of_nums))
#def smallest():


