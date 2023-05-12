"""
defines various models (user,usergroup) project (list)
"""
# Import necessary modules
from flask_login import UserMixin
from flask import current_app
from db import get_db


class User(UserMixin):
    """Define a User class that inherits from the UserMixin class"""
    def __init__(self, id, username, email, password, is_admin, user_group_id):
        """init user class"""
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.is_admin = is_admin
        self.user_group_id = user_group_id
        self.theme = 'light'

    @staticmethod
    def get(user_id):
        """Define a static method to get a user based on their ID"""
        db = get_db(current_app)
        c = db.cursor()
        c.execute('SELECT * FROM users WHERE id=?', (user_id,))
        user = c.fetchone()
        db.close()

        if user:
            return User(user[0], user[1], user[2], user[3], user[4], user[5])
        return None

    @staticmethod
    def find_by_username(username):
        """Define a static method to find a user based on their username"""
        conn = get_db()
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username=?', (username,))
        user = c.fetchone()
        conn.close()

        if user:
            return User(user[0], user[1], user[2], user[3], user[4], user[5])
        return None

    @staticmethod
    def get_all_users(user_objs):
        """Retrieve all users from the database"""
        conn = get_db()
        c = conn.cursor()
        c.execute('SELECT * FROM users')
        users = c.fetchall()
        conn.close()

        user_objs = []
        for user in users:
            user_obj = User(
                user[0], user[1], user[2],
                user[3], user[4], user[5]
                )
            user_objs.append(user_obj)

        return user_objs


class UserGroup:
    """Define a UserGroup class"""
    def __init__(self, id, name, created_by_admin):
        """init function"""
        self.id = id
        self.name = name
        self.created_by_admin = created_by_admin

    @staticmethod
    def get(user_group_id):
        """Define a static method to get a user group based on its ID"""
        db = get_db(current_app)
        c = db.cursor()
        c.execute('SELECT * FROM user_groups WHERE id=?', (user_group_id,))
        user_group = c.fetchone()
        db.close()

        if user_group:
            return UserGroup(user_group[0], user_group[1], user_group[2])
        return None

    @staticmethod
    def create(name, created_by_admin):
        """Define a static method to create a new user group"""
        conn = get_db()
        c = conn.cursor()
        c.execute(
            'INSERT INTO user_groups (name, created_by_admin) VALUES (?, ?)',
            (name, created_by_admin))
        conn.commit()
        user_group_id = c.lastrowid
        conn.close()

        return UserGroup(user_group_id, name, created_by_admin)

    @staticmethod
    def find_by_name(name):
        """Define a static method to find a user group based on its name"""
        conn = get_db()
        c = conn.cursor()
        c.execute('SELECT * FROM user_groups WHERE name=?', (name,))
        user_group = c.fetchone()
        conn.close()

        if user_group:
            return UserGroup(user_group[0], user_group[1], user_group[2])
        return None

class Projects:
    """Define a Project class"""
    def __init__(self, id, name, description, tasks, goals):
        """init function"""
        self.id = id
        self.name = name
        self.description = description
        self.tasks = tasks
        self.goals = goals

    @staticmethod
    def get_all_projects(project_objs):
        """Retrieve all projects from the database"""
        conn = get_db()
        c = conn.cursor()
        c.execute('SELECT * FROM projects')
        projects = c.fetchall()
        conn.close()

        project_objs = []
        for project in projects:
            project_obj = Projects(project[0], project[1], project[2],project[3], project[4])
        project_objs.append(project_obj)

        return project_objs