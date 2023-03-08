from flask import Flask, render_template, request, redirect
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


app = Flask(__name__)
@app.route("/")
def index():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `Todo_Database` ORDER BY `Completed` DESC")
    results = cursor.fetchall()
    
    return render_template("todo.html.jinja", 
                           todos = results)


@app.route("/add", methods=['POST'])
def add():
    new_todo = request.form['new_todo']
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO `Todo_Database` (`Description`) VALUES ('{new_todo}');")
    return redirect("/")
