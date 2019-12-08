import pymysql
#database connection
connection=pymsql.connect(host="localhost",user="root",passwd="",database="Employee")
cursor=connection.cursor()
#query for creatig table 
EmpTableSql="""CREATE TABLE Besant(
ID INT(20) PRIMARY KEY AUTO_INCREMENT,
EMPID INT(20),
NAME CHAR(20) NOT NULL,
DESIGNATION CHAR(20),
EXPERIENCE INT(20),
SALARY INT(20))"""
cursor.execute(EmpTableSql)
connection.cloe()
