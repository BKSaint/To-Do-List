from flask import Flask, render_template, request

app = Flask(__name__)
todos = ["go to the store", "buy groceries", "eat lunch"]
@app.route("/")
def index():
    return render_template("todo.html.jinja")


@app.route("/app")
def add():
    new_todo = request.form['new_todo']
    todos.append(new_todo)