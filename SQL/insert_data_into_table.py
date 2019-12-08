import pymysql
connection=pymysql.connect(host="localhost",user="root",passwd="",database="Employee")
cursor=connection.cursor()
#queries for inserting values
insert1="INSERT INTO Besant(EMPID,NAME,DESIGNATION,EXPERIENCE,SALARY) VALUES(1004,'Sony','QA',2,2000000);"
insert2="INSERT INTO Besant(EMPID,NAME,DESIGNATION,EXPERIENCE,SALARY) VALUES(1007,'Arpita','DEV',3,3000001);"
insert3="INSERT INTO Besant(EMPID,NAME,DESIGNATION,EXPERIENCE,SALARY) VALUES(1009,'Das','SW',20,4000002);"
insert4="INSERT INTO Besant(EMPID,NAME,DESIGNATION,EXPERIENCE,SALARY) VALUES(1012,'Moni','Firmware',10,5000003);"
cursor.execute(insert1)
cursor.execute(insert2)
cursor.execute(insert3)
cursor.execute(insert4)
connection.commit()
connection.close()
