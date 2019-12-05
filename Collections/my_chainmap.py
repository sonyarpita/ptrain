from collections import ChainMap
dict1={'name':"" , 'surname':""  , 'company': ""}
dict1['name']=input("Enter name: ")
dict1['surname']=input("Enter surname: ") 
dict1['company']=input("Enter company name: ")
print(dict1)
dict2={'dept':"", 'design':"", 'salary':""}
dict2['dept']=input("Enter dept: ")
dict2['design']=input("Enter designation: ")
dict2['salary']=int(input("Enter salary: "))
print(dict2)
comb_dict=ChainMap(dict1,dict2)
print(comb_dict)
print(comb_dict.keys())
print(dict1.keys())
print(list(comb_dict.keys()))
dict3={'a':1,'b':2}
comb2_dict=comb_dict.new_child(dict3)
print(comb2_dict)
