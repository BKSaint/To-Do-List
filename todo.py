from flask import Flask, render_template, request, redirect
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

import pymysql
import pymysql.cursors
##


connection = pymysql.connect(
    host="10.100.33.60",
    user="swalker",
    password="221085269",
    database="swalker_Todo",
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True

)


app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "saint": generate_password_hash("saint05")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
        check_password_hash(users.get(username), password):
        return username


@app.route("/")
@auth.login_required

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

@app.route("/complete", methods=["POST"])
def complete():
    todo_id = request.form['todo_id']
    
    cursor = connection.cursor()
    cursor.execute(f"UPDATE `Todo_Database` SET `Completed` = 1 WHERE `ID` = {todo_id}")
    
    return redirect("/")