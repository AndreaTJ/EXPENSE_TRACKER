from application import db 

class Users(db.Model): 
    name = db.Column(db.String(50), nullable=False)
    email_address = db.Column(db.String(50), primary_key=True, unique = True, nullable=False)
    expenses = db.relationship('Expenses', backref='users')

class Expenses (db.Model):
    expense_id = db.Column(db.Integer, primary_key=True, unique = True, nullable=False)
    type_expense = db.Column(db.String(120), nullable=False)
    description_expense = db.Column(db.String(120), nullable=False)
    date_purchase = db.Column(db.DateTime, nullable = False) 
    amount = db.Column(db.Float, nullable = False)
    user_email = db.Column(db.String(50), db.ForeignKey('users.email_address'), nullable=False)

