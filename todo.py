from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("todo.html.jinja", 
                            todos = ["go to the store", "buy groceries", "eat lunch"])

@app.route("/app")
def add():
    new_todo = request.form['new_todo']