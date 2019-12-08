import pymysql
connection=pymysql.connect(host="localhost",user="root",passwd="",database="Employee")
cursor=connection.cursor()
#queries for inserting values
insert1="DROP TABLE IF EXISTS Besant;"
cursor.execute(insert1)
connection.commit()
connection.close()
