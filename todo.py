from flask import Flask, render_template, request, redirect

app = Flask(__name__)
my_todos = ["go to the store", "buy groceries", "eat lunch"]
@app.route("/")
def index():
    return render_template("todo.html.jinja", 
                           todos = my_todos)


@app.route("/add", methods=['POST'])
def add():
    new_todo = request.form['new_todo']
    my_todos.append(new_todo)
    return redirect("/")
