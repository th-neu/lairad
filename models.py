# Import necessary modules
from flask_login import UserMixin
from flask import current_app
from db import get_db


# Define a User class that inherits from the UserMixin class
class User(UserMixin):
    def __init__(self, id, username, email, password, is_admin, user_group_id):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.is_admin = is_admin
        self.user_group_id = user_group_id
        self.theme = 'light'

    # Define a static method to get a user based on their ID
    @staticmethod
    def get(user_id):
        db = get_db(current_app)
        c = db.cursor()
        c.execute('SELECT * FROM users WHERE id=?', (user_id,))
        user = c.fetchone()
        db.close()

        if user:
            return User(user[0], user[1], user[2], user[3], user[4], user[5])
        else:
            return None

    # Define a static method to find a user based on their username
    @staticmethod
    def find_by_username(username):
        conn = get_db()
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username=?', (username,))
        user = c.fetchone()
        conn.close()

        if user:
            return User(user[0], user[1], user[2], user[3], user[4], user[5])
        else:
            return None


# Define a UserGroup class
class UserGroup:
    def __init__(self, id, name, created_by_admin):
        self.id = id
        self.name = name
        self.created_by_admin = created_by_admin

    # Define a static method to get a user group based on its ID
    @staticmethod
    def get(user_group_id):
        db = get_db(current_app)
        c = db.cursor()
        c.execute('SELECT * FROM user_groups WHERE id=?', (user_group_id,))
        user_group = c.fetchone()
        db.close()

        if user_group:
            return UserGroup(user_group[0], user_group[1], user_group[2])
        else:
            return None

    # Define a static method to create a new user group
    @staticmethod
    def create(name, created_by_admin):
        conn = get_db()
        c = conn.cursor()
        c.execute(
            'INSERT INTO user_groups (name, created_by_admin) VALUES (?, ?)',
            (name, created_by_admin))
        conn.commit()
        user_group_id = c.lastrowid
        conn.close()

        return UserGroup(user_group_id, name, created_by_admin)

    # Define a static method to find a user group based on its name
    @staticmethod
    def find_by_name(name):
        conn = get_db()
        c = conn.cursor()
        c.execute('SELECT * FROM user_groups WHERE name=?', (name,))
        user_group = c.fetchone()
        conn.close()

        if user_group:
            return UserGroup(user_group[0], user_group[1], user_group[2])
        else:
            return None
