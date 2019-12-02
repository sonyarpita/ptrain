num_of_nums=int(input("Enter number of numbers to be sorted: "))
user_input_num_list=[]

def enter_list_elements(x):
    for i in range(x):
        i=int(input("Enter elements: "))
        user_input_num_list.append(i)

enter_list_elements(num_of_nums)
print("Largest Number=",max(user_input_num_list))
print("Smallest Number=",min(user_input_num_list))
print(user_input_num_list.index(2)) # Checks if the entered list contains the element 2 
