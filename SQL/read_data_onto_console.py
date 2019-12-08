import pymysql
connection=pymysql.connect(host="localhost",user="root",passwd="",database="Employee")
cursor=connection.cursor()
#queries for inserting values
insert1="SELECT * from Besant;"
cursor.execute(insert1)
records=cursor.fetchall()
for record in records:
	print(record)
#connection.commit()
connection.close()
