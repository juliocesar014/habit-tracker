from flask import Flask, render_template, url_for, request, redirect
from db import db

app = Flask(__name__)
habits = ['Test Habit','Tets Habit 2']


@app.route("/")
def index():
    return render_template("index.html", habits=habits ,title = "Habit Tracker - Home")


@app.route("/add", methods=["GET", "POST"])
def add_habit():
    if request.method == "POST":
        habit = request.form.get("habit")
        habits.append(habit)
        return redirect(url_for('index'))
    else:
        error = 'Invalid Habit Tracker'
        return render_template("add_habit.html", title = "Habit Tracker - Add new", error=error)
    


if __name__ == '__main__':
    app.run(debug=True)
    
    
