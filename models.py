"""
defines various models (user,usergroup) project (list) / prompt
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
    def get_all_projects():
        """Retrieve all projects from the database"""
        conn = get_db()
        c = conn.cursor()
        c.execute('SELECT * FROM projects')
        projects = c.fetchall()

        project_objs = []
        for project in projects:
            project_obj = Projects(
                               project[0], project[1],
                               project[2], project[3], project[4]
                               )
            project_objs.append(project_obj)

        return project_objs

    @staticmethod
    def get_task_from_database():
        """get task from database"""
        conn = get_db()
        c = conn.cursor()
        c.execute('SELECT tasks FROM projects')
        c.fetchall()
        conn.close()
        tasks = []
        if tasks:
            return tasks(project[3])
        return None

    @staticmethod
    def get_goals_from_database():
        """get task from database"""
        conn = get_db()
        c = conn.cursor()
        c.execute('SELECT * FROM projects LIMIT 1')
        goal = c.fetchone()


        if goal:
            # Assuming the prompt text is in columns 2, 3, and 4
            goal_text = (goal[4])
            return goal_text
        return ""


class Prompts:
    """Define a Prompt class"""
    def __init__(
                 self, id, intro, constraints, commands,
                 resources, performance_eval,
                 response_form, outro, model
                ):
        """init function"""
        self.id = id
        self.intro = intro
        self.constraints = constraints
        self.commands = commands
        self.resources = resources
        self.performance_eval = performance_eval
        self.response_form = response_form
        self.outro = outro
        self.model = model

    @staticmethod
    def get_all_prompts():
        """Retrieve all prompts from the database"""
        conn = get_db()
        c = conn.cursor()
        c.execute('SELECT * FROM prompts')
        prompts = c.fetchall()
        conn.close()

        prompt_objs = []
        for prompt in prompts:
            prompt_obj = Prompts(
                                   prompt[0], prompt[1], prompt[2],
                                   prompt[3], prompt[4], prompt[5],
                                   prompt[6], prompt[7], prompt[8]
                                   )
            prompt_objs.append(prompt_obj)
        return prompt_objs

    def get_prompt_from_database():
        """get prompt from database"""
        conn = get_db()
        c = conn.cursor()
        c.execute('SELECT * FROM prompts LIMIT 1')
        prompt = c.fetchone()

        if prompt:
            # Assuming the prompt text is in columns 2, 3, and 4
            prompt_text = ' '.join(prompt[1:8])
            return prompt_text
        return ""

    def get_prompt_first_part():
        """get prompt first part"""
        conn = get_db()
        c = conn.cursor()
        c.execute('SELECT * FROM prompts LIMIT 1')
        prompt = c.fetchone()

        if prompt:
            # Assuming the prompt text is in columns 2, 3, and 4
            prompt_text = (prompt[1])
            return prompt_text
        return ""

    def get_prompt_second_part():
        """get prompt second part"""
        conn = get_db()
        c = conn.cursor()
        c.execute('SELECT * FROM prompts LIMIT 1')
        prompt2 = c.fetchone()

        if prompt2:
            # Assuming the prompt text is in columns 2, 3, and 4
            prompt2_text = ' '.join(prompt2[2:8])
            return prompt2_text
        return ""


class Thoughts:
    """Define a Thoughts class"""
    def __init__(
                 self, id, project_id, thought_text, reasoning_text,
                 plan, criticism, command, command_args
                ):
        """init function"""
        self.id = id
        self.project_id = project_id
        self.thought_text = thought_text
        self.reasoning_text = reasoning_text
        self.plan = plan
        self.criticism = criticism
        self.command = command
        self.command_args = command_args
