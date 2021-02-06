from application import app, db
from flask import render_template, request, url_for, redirect
from application.models import Users, Expenses
from application.forms import AddUser, AddExpense, ModExpense
from datetime import date

@app.route('/')
def home(): 
    count_users = Users.query.count()
    if count_users==0: 
        return render_template("home.html")
    else: 
        users = Users.query.all() 
        return render_template("home.html", users=users)

@app.route('/add_user', methods=['GET', 'POST'])
def adding_new_users():

    form = AddUser (request.form)

    if request.method == 'GET':
        return render_template("add_user.html", form=form)
    else:
        try: 
            new_user = Users (name = request.values.get ("Name"), email_address = request.values.get ("Email_address") )
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("home"))

        except Exception as e:
            error= "" 
            if "users.email_address" in str(e): 
                    error = "This email is already in use, please use a different email"
            else: 
                    error = "This name is already in use, please use a different name"
            return render_template('add_user.html', form=form, error_db_insert=error)
        

@app.route('/expenses')
def show_expenses():
    name_user = request.values.get("user")

    if name_user ==None: 
        return redirect (url_for("home"))
    else: 

        expenses_user = db.session.query(Expenses).join(Users).filter(Users.name ==name_user).all()
    
        if expenses_user==[]: 
            return render_template("expenses.html", name_user = name_user)
        else: 
            query = Expenses.query.filter (Expenses.user_name== name_user).all()
                
            Total_amount = 0
            for data in query: 
                data.amount
                Total_amount +=data.amount
            total_amount = round(Total_amount,2)

            return render_template("expenses.html", expenses=expenses_user, name_user = name_user, total =total_amount) 

@app.route('/add_expense', methods=['GET', 'POST'] )
def adding_new_expenses():
    
    name_user = request.values.get("user")

    if name_user ==None: 
        return redirect (url_for("home"))
    else: 
        form = AddExpense(request.form)

        if request.method == 'GET':
            return render_template("add_expense.html", form=form)
        else:
            if form.validate (): 

                new_expense = Expenses (type_expense= request.values.get ("Type"), 
                description_expense = request.values.get ("Description"), 
                date_purchase = request.values.get ("Date"), 
                amount = request.values.get ("Amount"), 
                user_name = name_user ) 

                db.session.add(new_expense)
                db.session.commit()
                       
                return redirect(url_for("show_expenses", user = name_user))

                
            else: 
                return render_template("add_expense.html", form=form)

@app.route('/mod_expense', methods=['GET', 'POST'] )
def modifying_expenses():   
    name_user = request.values.get("user")
    expense_id = request.values.get ("id")

    if name_user == None or expense_id == None: 
        return redirect (url_for("home"))
    else: 

        query = db.session.query (Expenses).filter (Expenses.expense_id == expense_id)

        for data in query: 
            type_expense = data.type_expense
            description_expense = data.description_expense
            date_purchase = data.date_purchase
            amount = data.amount

        if request.method == 'GET':
            form = ModExpense (data= {"Type" : type_expense,
                                    "Description": description_expense,
                                    "Date": date (int(date_purchase[:4]), int(date_purchase[5:7]), int(date_purchase[8:])),
                                    "Amount":amount })
            return render_template("mod_expense.html", form=form)
        else:

            form = ModExpense (request.form)

            if request.form.get ("Delete"): 

                query3 = Expenses.query.filter (Expenses.expense_id == expense_id).first() 
                db.session.delete (query3)
                db.session.commit() 
                return redirect(url_for("show_expenses", user = name_user))

            if form.validate(): 
            
                if request.form.get ("Save_changes"): 
                    query2 = Expenses.query.filter (Expenses.expense_id == expense_id).all()
                    for element in query2: 
                        element.type_expense = form.Type.data
                        element.description_expense = form.Description.data 
                        element.date_purchase = form.Date.data
                        element.amount = form.Amount.data 
                    db.session.commit() 
                
                    return redirect(url_for("show_expenses", user = name_user))
            else: 
                return render_template("mod_expense.html", form=form)

       




