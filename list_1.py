empDetails={
	"name":"Besant",
	"id":420,
	"salary":50000
}
print(empDetails)
print(empDetails['name'])
print("****************")
print("Length is:",len(empDetails))
print("****************")
sta="name" in empDetails
print("sta is",sta)
sta1="bes" not in empDetails
print("sta1 is",sta1)
print("****************")
print(empDetails.keys())
print("****************")
print(empDetails.values())
print("****************")
print(empDetails.items())
print("****************")
print(empDetails.get("name"))
print("****************")
print(empDetails.pop('name'))
print("****************")
print(empDetails.popitem())
copy_empDetails=empDetails.copy()
print("****************")
print(copy_empDetails)
print("****************")
copy_empDetails.clear()
print(copy_empDetails)
