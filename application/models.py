from application import db 
import datetime

class Users(db.Model): 
    name = db.Column(db.String(50), primary_key=True, unique = True, nullable=False)
    email_address = db.Column(db.String(50), nullable=False, unique = True)
    expenses = db.relationship('Expenses', backref='users')

class Expenses (db.Model):
    expense_id = db.Column(db.Integer, primary_key=True, unique = True, nullable=False)
    type_expense = db.Column(db.String(120), nullable=False)
    description_expense = db.Column(db.String(120), nullable=False)
    date_purchase = db.Column(db.String(10), nullable = False) 
    amount = db.Column(db.Float, nullable = False)
    user_name = db.Column(db.String(50), db.ForeignKey('users.name'), nullable=False)

