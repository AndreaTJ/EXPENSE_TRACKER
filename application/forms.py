from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, SelectField, FloatField, HiddenField
from wtforms.fields.html5 import EmailField, DateField
from wtforms.validators import DataRequired, Length, ValidationError


class AddUser(FlaskForm):
    Name = StringField('First Name', validators=[DataRequired(), Length(min=4, max=15)]) 
    Email_address = EmailField('Email', validators=[DataRequired()]) 
    Submit = SubmitField('Add new user')


Type_of_expense =["Personal", "House", "Transport", "Pets", "Miscellaneous"]

class AddExpense(FlaskForm):
    Expense_id = HiddenField("id")
    Type= SelectField('Type of expense', choices=[(typ, typ) for typ in Type_of_expense])
    Description = StringField('Description of the expense.', validators=[DataRequired()])
    Date= DateField('Purchase Date', format='%Y-%m-%d', validators=[DataRequired()])
    Amount = FloatField('Amount (£)', validators=[DataRequired(message="Invalid amount. Please, introduce a positive number")])

    Add = SubmitField('Add new expense')

    def validate_Amount (self, Amount): 
        if Amount.data <= 0: 
            raise ValidationError ("Invalid amount, please introduce a number greater than 0")




class ModExpense(FlaskForm):
    Expense_id = HiddenField("id")
    Type= SelectField('Type of expense', choices=[(typ, typ) for typ in Type_of_expense])
    Description = StringField('Description of the expense.', validators=[DataRequired()])
    Date= DateField('Purchase Date', format='%Y-%m-%d', validators=[DataRequired()])
    Amount = FloatField('Amount (£)', validators=[DataRequired(message="Invalid amount. Please, introduce a positive number")])

    Save_changes = SubmitField('Save Changes')
    Delete = SubmitField('Delete Expense')

    def validate_Amount (self, Amount): 
        if Amount.data <= 0: 
            raise ValidationError ("Invalid amount, please introduce a number greater than 0")
        
