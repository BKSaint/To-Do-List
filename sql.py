import pymysql
import pymysql.cursors

connection = pymysql.connect(
    host="10.100.33.60",
    user="swalker",
    password="221085269",
    database="swalker_Todo",
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM `Todo_Database`")
result = cursor.fetchall()
print(result)