import pymysql
connection=pymysql.connect(host="localhost",user="root",passwd="",database="Employee")
cursor=connection.cursor()
#queries for inserting values
insert1="UPDATE Besant SET NAME= 'Susmita' WHERE ID ='9';"
cursor.execute(insert1)
connection.commit()
connection.close()
