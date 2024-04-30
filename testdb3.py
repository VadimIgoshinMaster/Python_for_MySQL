import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="qwerty123",
    database="testdb"

)

mycursor = mydb.cursor()

sql1 = "SELECT * FROM students ORDER BY name DESC"

mycursor.execute(sql1)


myresult= mycursor.fetchall()


for row in myresult:
    print(row)


mydb.commit()  