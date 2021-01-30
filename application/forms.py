from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, SelectField, DateField, FloatField
from wtforms.validators import DataRequired, Length, ValidationError, Email


class AddUser(FlaskForm):
    Name = StringField('First Name', validators=[DataRequired(), Length(min=4, max=15)]) 
    Email_address = StringField('Email', validators=[Email(), Length(min=5)])
    Submit = SubmitField('Add new user')


Type_of_expense =["Personal", "House", "Transport", "Pets", "Miscellaneous"]

class AddExpense(FlaskForm):
    Type= SelectField('Type of expense', choices=[(typ, typ) for typ in Type_of_expense])
    Description = StringField('Description of the expense.', validators=[DataRequired()])
    Date_= DateField("Date", format='%Y-%m-%d',validators=[DataRequired()])
    Amount = FloatField('Amount', validators=[DataRequired()])

    Add = SubmitField('Add new expense')

    def validate_Amount (self, Amount): 
        if Amount.data <= 0: 
            raise ValidationError ("Invalid amount, please introduce a number greater than 0")


