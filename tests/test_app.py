import unittest 
from flask_testing import TestCase
from flask import url_for, request

from application import app, db
from application.models import Users, Expenses

class TestBase (TestCase):

    def create_app (self): 
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
        TESTING = True,
        WTF_CSRF_ENABLED = False)

        return app 

    def setUp (self): 
        db.create_all()
        
        self.new_user = Users (name = "Brad", email_address = "BJones@gmail.com" )
        self.new_expense = Expenses (type_expense = "Pets", 
                                description_expense = "Cat Food", 
                                date_purchase = "2021-12-22",
                                amount = 3.44,
                                user_name = "Brad") 
        db.session.add (self.new_user)
        db.session.add (self.new_expense)
        
        db.session.commit()

        
 
    def tearDown (self):
        db.session.remove()
        db.drop_all()

class TestAccess (TestBase): 
    def test_access_home (self): 
        response = self.client.get (url_for("home"))
        self.assertEqual (response.status_code, 200)
    def test_access_adduser (self): 
        response = self.client.get (url_for("adding_new_users"))
        self.assertEqual (response.status_code, 200)
    def test_access_expenses (self): 
        response = self.client.get (url_for("show_expenses"))
        self.assertEqual (response.status_code, 302)
    def test_access_add_expenses (self): 
        response = self.client.get (url_for("adding_new_expenses"))
        self.assertEqual (response.status_code, 302)
    def test_access_mod_expenses (self): 
        response = self.client.get (url_for("modifying_expenses"))
        self.assertEqual (response.status_code, 302)


class TestNoUser (TestBase): 

    def test_find_user(self): 
        
        response = self.client.get (url_for("home"))
        self.assertIn(b'Brad', response.data)
    
    def test_no_user(self): 
        num_rows_deleted = db.session.query(Users).delete()
        db.session.commit()

        response = self.client.get (url_for("home"))
        self.assertIn(b'Ready to track your expenses', response.data)

class Test_Show_Expenses (TestBase): 

    def test_expenses(self): 
        
        response = self.client.get ("/expenses?user=Brad") 
        self.assertIn(b'Action', response.data)
    
    def test_no_expenses(self): 
        num_rows_deleted = db.session.query(Expenses).delete()
        db.session.commit()
        
        response = self.client.get ("/expenses?user=Brad") 
        self.assertIn(b'Brad, would you like to start adding expenses?', response.data)

class Test_Add_Expenses (TestBase): 

    def test_add_new_expense(self): 
        
        response = self.client.get ("/add_expense?user=Brad") 
        self.assertIn(b'Add new expense', response.data)
    
class Test_Mod_Expenses (TestBase): 

    def test_mod_expense(self): 
        
        response = self.client.get ("/mod_expense?user=Brad&id=1") 
        self.assertIn(b'Delete Expense', response.data)
        
class Test_Post_User (TestBase): 

    def test_post_user(self): 
        response = self.client.post ((url_for("adding_new_users")),
                                    data = dict(Name = "Charlie", Email_address = "CWhite@gmail.com"), 
                                    follow_redirects=True)
        self.assertIn(b'Charlie', response.data)


    def test_post_user_duplicate(self): 
        response = self.client.post ((url_for("adding_new_users")),
                                    data = dict(Name = "Charlie", email_address = "CWhite@gmail.com"), 
                                    follow_redirects=True)
        self.assertIn(b'This email is already in use, please use a different email', response.data)

    def test_post_email_duplicate(self): 
        response = self.client.post ((url_for("adding_new_users")),
                                    data = dict(name= "Charlie", Email_address = "CWhite@gmail.com"), 
                                    follow_redirects=True)
        self.assertIn(b'This name is already in use, please use a different name', response.data)

class Test_Post_New_Expenses (TestBase): 

    def test_post_new_expenses(self): 
        response = self.client.post (("/add_expense?user=Brad"),
                                    data = dict(
                                    Type = "Personal",
                                    Description = "Black Plain T-shirt",
                                    Date = "2021-01-01",
                                    Amount = 6.99), 
                                    follow_redirects=True)
        self.assertIn(b'Black Plain T-shirt', response.data)
class Test_Post_New_Expenses_Error (TestBase): 

    def test_post_new_expenses_error(self): 
        response = self.client.post (("/add_expense?user=Brad"),
                                    data = dict(
                                    Type = "Personal",
                                    Description = "Black Plain T-shirt",
                                    Date = "2021-01-01",
                                    Amount = "sasdasd"))
        self.assertIn(b'Invalid amount. Please, introduce a positive number', response.data)

class Test_Post_New_Expenses_Negative (TestBase): 

    def test_post_new_expenses_negative(self): 
        response = self.client.post (("/add_expense?user=Brad"),
                                    data = dict(
                                    Type = "Personal",
                                    Description = "Black Plain T-shirt",
                                    Date = "2021-01-01",
                                    Amount = -50))
        self.assertIn(b'Invalid amount, please introduce a number greater than 0', response.data)
class Test_Post_Delete_Expenses (TestBase): 

    def test_post_del_expenses(self): 
            response = self.client.post (("/mod_expense?user=Brad&id=1"),
                                        data = dict(
                                        Delete = True), 
                                        follow_redirects=True)
            self.assertIn(b'Brad, would you like to start adding expenses', response.data)

class Test_Post_Mod_Expenses (TestBase): 

    def test_post_mod_expenses(self): 
            response = self.client.post (("/mod_expense?user=Brad&id=1"),
                                        data = dict(
                                        Expense_id =1, 
                                        Type = "Pets", 
                                        Description = "Dog Food",
                                        Date = "2021-12-22",
                                        Amount = 6.25,
                                        Save_changes = True), 
                                        follow_redirects=True)
            self.assertIn(b'6.25', response.data)
            self.assertIn(b'Dog Food', response.data)

class Test_Post_Mod_Expenses_Error (TestBase): 

    def test_post_mod_expenses_error(self): 
            response = self.client.post (("/mod_expense?user=Brad&id=1"),
                                        data = dict(
                                        Expense_id =1, 
                                        Type = "Pets", 
                                        Description = "Dog Food",
                                        Date = "2021-12-22",
                                        Amount = "sss",
                                        Save_changes = True))
            self.assertIn(b'Invalid amount. Please, introduce a positive number', response.data)

class Test_Post_Mod_Expenses_Negative (TestBase): 

    def test_post_mod_expenses_negative(self): 
            response = self.client.post (("/mod_expense?user=Brad&id=1"),
                                        data = dict(
                                        Expense_id =1, 
                                        Type = "Pets", 
                                        Description = "Dog Food",
                                        Date = "2021-12-22",
                                        Amount = -34,
                                        Save_changes = True))
            self.assertIn(b'Invalid amount, please introduce a number greater than 0', response.data)

            