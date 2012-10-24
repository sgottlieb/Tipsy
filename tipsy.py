from flask import Flask, render_template, request, redirect
import model

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", user_name="sara_and_lydia")

@app.route("/tasks")
def list_tasks():
    db = model.connect_db()
    tasks_from_db = model.get_tasks(db, None)
    return render_template("list_tasks.html", tasks=tasks_from_db)

@app.route("/new_task")
def new_tasks():
    # db = model.connect_db()
    # new_task_form= model.new_task(db, )
    return render_template("new_task.html")

@app.route("/save_task", methods=["POST"])
def save_task():
    task_title = request.form['task_title']
    db = model.connect_db()
    task_id = model.new_task(db, task_title, 1)
    tasks_from_db = model.get_tasks(db, None)
    return render_template("list_tasks.html", tasks=tasks_from_db)

@app.route("/complete_task", methods=["POST"])
def complete_task():
    task_complete = request.form['complete']
    db = model.connect_db()
    task_id = model.complete_task(db,task_complete)
    return list_tasks()


if __name__ == "__main__":
    app.run(debug=True)