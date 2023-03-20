from login_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from login_app import DATABASE , bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Register:
    def __init__(self,data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        

    @classmethod
    def create(cls,form):

        
        hashed_pw = bcrypt.generate_password_hash(form['password'])
        data = {
            **form,
            'password' : hashed_pw
        }

        query = """
            INSERT INTO user(first_name,last_name,email,password) 
            VALUES (%(first_name)s ,%(last_name)s , %(email)s , %(password)s)

        """
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one_email(cls,email):

        data = {
            'email' : email,
        }

        query = "SELECT * FROM user WHERE email = %(email)s;"

        results = connectToMySQL(DATABASE).query_db(query, data)

        if results:
            user = cls(results[0])

            return user
        else :
            return False







    @classmethod
    def validate(cls,form):

        is_valid = True

        if len(form['first_name']) < 3 or len(form['first_name']) == 0 :
            is_valid = False
            flash('First Name is too short!!!!!!')
        
        if len(form['last_name']) < 3:
            is_valid = False
            flash('Last Name is too short!!!!!!')
        
        if not EMAIL_REGEX.match(form['email']):
            is_valid = False
            flash('Invalid Email format!!!!!!')

        if cls.get_one_email(form['email']):
            is_valid = False
            flash('Email has already been registered, please pick another!!!')

        if len(form['password']) < 8 :
            is_valid = False
            flash('Password must be at least 6 characters!!!')

        if form['password'] != form['confirm_password']:
            is_valid  = False
            flash('Password must match!!!')


        return is_valid

    @classmethod
    def validate_login(cls,form):

        found_user = cls.get_one_email(form['email'])

        if found_user:
            if bcrypt.check_password_hash(found_user.password , form['password']):
                return found_user
            
        else:
            flash('Invalid Login')
            return False