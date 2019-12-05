from collections import OrderedDict
fruits_type=OrderedDict([
	("Apples",200),
	("Watermelons",150),
	("Grapes",100),
	("Mangoes",100)
])
print(fruits_type.items())
for key,value in fruits_type.items():
	print(key,value)
