from application import app
from flask import render_template

@app.route('/')
def home(): 
    return render_template ("home.html")

@app.route('/add_user')
def adding_new_users():
    return render_template ("add_user.html")

@app.route('/expenses')
def show_expenses():
    return render_template ("expenses.html")

@app.route('/add_expense')
def adding_new_expenses():
    return render_template ("add_expense.html")