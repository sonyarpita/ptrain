import pymysql
connection=pymysql.connect(host="localhost",user="root",passwd="",database="Employee")
cursor=connection.cursor()
#queries for inserting values
insert1="DELETE FROM Besant WHERE ID ='10';"
cursor.execute(insert1)
connection.commit()
connection.close()
