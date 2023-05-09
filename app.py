"""
main lairad app, provides login/lougout and main routes
"""

# Import the required packages
import os
from flask import Flask, render_template, request, url_for, redirect, current_app
from flask_login import login_required, LoginManager, current_user, login_user
from flask_login import UserMixin, logout_user
from flask_login.mixins import AnonymousUserMixin
from werkzeug.urls import url_parse
# import User model and database connection from other files
from models import User
from db import get_db
from theme import theme_bp
from routes.project import project_bp

# Create a Flask application instance
app = Flask(__name__)
app.register_blueprint(project_bp, app=app)

# Set the Flask secret key from an environment variable
app.secret_key = os.getenv('SECRET_KEY')

# Set the LOGIN_DISABLED flag to False by default
app.config['LOGIN_DISABLED'] = False  # set to True if user is not logged in

# Create a login manager instance and initialize it with the Flask app instance
login_manager = LoginManager()
login_manager.init_app(app)

# Register the blueprint from the theme module
app.register_blueprint(theme_bp)

# Register the blueprint from the add_project module


class AnonymousUser(AnonymousUserMixin):
    """Define an anonymous user class for the login manager to use"""
    id = None
    is_active = False
    is_authenticated = False
    username = 'Guest'
    theme = 'light'


# Set the anonymous user for the login manager
login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(user_id):
    """login manager / loads user from database using the user_id"""
    conn = get_db(app)
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE id=?', (user_id,))
    user = c.fetchone()
    # conn.close()

    if not user:
        return None

    user_obj = UserMixin()
    user_obj.id = user[0]
    user_obj.username = user[1]
    user_obj.password = user[2]
    user_obj.theme = user[3]
    user_obj.is_admin = user[4]
    return user_obj


@login_manager.unauthorized_handler
def unauthorized():
    """Define an unauthorized handler function for the login manager"""
    return redirect(url_for('login', next=request.endpoint))


# Project listing route
# @app.route('/project/<projects_id>', methods=['GET', 'POST'])
# def project(projects_id):
#   conn = get_db(app)
#   c = conn.cursor()
#   c.execute('SELECT * FROM projects WHERE id=?', (projects_id,))
#   project_id = project[0]


@app.errorhandler(404)
def not_found_error(e):
    """404 error handler"""
    return render_template('404.html'), 404


@app.route('/add_user', methods=['GET', 'POST'])
@login_required
def add_user():
    """Define a route for adding a user to the database"""
    if not current_user.is_admin:
        return redirect(url_for('home'))

    if request.method == 'POST':
        # Get the user details from the form
        username = request.form['username']
        password = request.form['password']
        is_admin = request.form.get('is_admin') == 'True'

        # Save the user details to the database
        conn = get_db(app)
        c = conn.cursor()
        c.execute(
            'INSERT INTO users (username, password, is_admin)'
            'VALUES (?, ?, ?)',
            (username, password, is_admin))
        conn.commit()
        conn.close()

        return redirect(url_for('home'))

    # Render the add user form
    return render_template('add_user.html')


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    """defines a logout route"""
    # Log the user out
    logout_user()

    # Redirect the user to the login page
    return redirect(url_for('login'))


@app.route('/', methods=['GET', 'POST'])
def login():
    """main route"""
    # Check if the user is already authenticated
    if current_user.is_authenticated:
        # If so, redirect them to the home page
        return redirect(url_for('home'))

    if request.method == 'POST':
        # Connect to the database
        # db = get_db(app)
        # Get the username and password from the form
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password are correct
        conn = get_db(app)
        c = conn.cursor()
        c.execute(
            'SELECT * FROM users WHERE username=? AND password=?',
            (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            # If the username and password are correct, log the user in
            user_obj = User(
                user[0], user[1], user[2],
                user[3], user[4], user[5]
                )
            login_user(user_obj)

            # Redirect the user to the original page they were trying to access
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('home')
            return redirect(next_page)
            # If the username and password are incorrect, show an error message
        error = 'Invalid username or password. Please try again.'
        return render_template('login.html', error=error)
    # else:
    # If the request method is GET, show the login page
    return render_template('login.html')


@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    """homme route"""
    db = get_db(app)
    if request.method == 'POST':
        # Retrieve the user's selected theme from the form
        theme = request.form.get('theme')
        # Connect to the database
        conn = db.get_db()
        c = conn.cursor(dictionary=True)
        # Update the user's theme in the database
        c.execute("""
            UPDATE users SET theme = ? WHERE id = ?
        """, [theme, current_user.id])
        conn.commit()
        # Set the current user's theme to the selected theme
        current_user.theme = theme
    # Render the home page with the current user's selected theme
    return render_template('index.html', theme=current_user.theme)


if __name__ == '__main__':
    app.run(debug=True)
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=5000)
