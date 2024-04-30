import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="qwerty123",
    database="testdb"

)

mycursor = mydb.cursor()

sql = "DELETE FROM students WHERE age = 19"

sql = "DROP TABLE IF EXISTS students"

mycursor.execute(sql)

mydb.commit()  