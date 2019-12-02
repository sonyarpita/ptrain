num_of_nums=int(input("Enter number of numbers to be sorted: "))
user_input_num_list=[]

def enter_list_elements(x):
        for i in range(x):
                i=int(input("Enter elements: "))
                user_input_num_list.append(i)
        return user_input_num_list

print("List: ",enter_list_elements(num_of_nums))

def smallest(list1):
    small=list1[0]
    for i in range(len(list1)):
        if list1[i] < small:
            small=list1[i]
    return small

def largest(list1):
    large=list1[0]
    for i in range(len(list1)):
        if list1[i] > large:
            large=list1[i]
    return large

print("Largest Element=",largest(user_input_num_list))
print("Smallest Element=",smallest(user_input_num_list))
