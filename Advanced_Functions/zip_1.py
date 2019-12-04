#Python code to demonstrate zip()
#initialize lists
name=["Sony","Arpita", "Das","Susmita"]
roll_no=[4,3,6,7]
marks=[90,98,89,99]
#using zip() to map values
mapped=zip(name,roll_no,marks)
#converting values to print as set
mapped=list(mapped)
#printing result values
print("Zipped result is: ",end=" ")
print(mapped)
