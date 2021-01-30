from application import app

@app.route('/')
def home(): 
    return "Users"

@app.route('/add_user')
def adding_new_users():
    return "Here, we will add new users"

@app.route('/expenses')
def show_expenses():
    return "Here, we will see the expenses, depending on the user"

@app.route('/add_expense')
def adding_new_expenses():
    return "Here, we will add new expenses, depending on the user"