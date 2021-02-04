import unittest 
from flask_testing import TestCase
from flask import url_for

from application import app, db
from application.models import Users, Expenses

class TestBase (TestCase):

    def create_app (self): 
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///data.db")
        return app 

    def setUp (self): 
        db.create_all()
        
        new_user = Users (name = "Tom2342", email_address = "Broaawwwwwn@s232" )
        db.session.add (new_user)
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
        self.assertIn(b'Tom2342', response.data)
        print(response.data)
    
    def test_no_user(self): 
        num_rows_deleted = db.session.query(Users).delete()
        db.session.commit()

        response = self.client.get (url_for("home"))
        self.assertIn(b'Ready to track your expenses', response.data)
        print(response.data)
   

class TestAddUser(TestBase): 
    def test_add_post(self):
        response = self.client.post( url_for('adding_new_users'),
                    data = dict(name="Charlie", email_address = "Charlie@gmail.com"),
                    follow_redirects=True)
        self.assertIn(b'Enter your name',response.data)
