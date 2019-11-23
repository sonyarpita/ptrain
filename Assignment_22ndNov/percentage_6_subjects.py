eng=float(input("ENter Mrks for English: "))
math=float(input("ENter Mrks for Math: "))
sci=float(input("ENter Mrks for Science: "))
his=float(input("ENter Mrks for History: "))
geo=float(input("ENter Mrks for Geography: "))
fre=float(input("ENter Mrks for French: "))
#Calculate %
add=eng+math+sci+his+geo+fre
print("Total Marks = ",add)
percentage=(add/600)*100
print("Percentge = ",percentage)
