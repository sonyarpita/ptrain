from collections import ChainMap
dict1={'a': 1, 'b': 2}
dict2={'c': 3, 'b': 4}
chain_map=ChainMap(dict1,dict2)
print(chain_map.maps)
print(chain_map['a'])
dict2['c']=5
print(chain_map.maps)
print(list(chain_map.keys()))
print(list(chain_map.values()))
dict3={'e':5, 'f': 6}
chain_map=chain_map.new_child(dict3) # adding new dictionary to ChainMap
print(chain_map)

