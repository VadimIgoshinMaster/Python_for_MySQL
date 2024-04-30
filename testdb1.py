import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="qwerty123",
    database="testdb"

)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE testdb")

mycursor.execute("SHOW DATABASES")

mycursor.execute("CREATE TABLE students (name VARCHAR(225), age INTEGER(10))")

mycursor.execute("SHOW TABES")

for db in mycursor:
    print(db)

for tb in mycursor:
    print(tb)

sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
student1 = ("Tim", 22)

mycursor.execute(sqlFormula, student1)

students = [("Anna", 17),
            ("Nick", 18),
            ("John", 19),
            ("Peter", 20)]

mycursor.executemany(sqlFormula, students)
mydb.commit()
