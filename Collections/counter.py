from collections import Counter
usr_list=[1,2,3,4,1,2,6,7,3,8,1]
count_obj=Counter(usr_list)
print("All element count= ",count_obj)
print("count 1 is",count_obj[1])
team_scores=[
	('India',89),
	('Australia',92),
	('England',99),
	('India',89)
]
count=Counter(team_scores)
print(count)
