# Import necessary modules
from flask import Blueprint, render_template, request, current_app
from flask_login import login_required, current_user
from models import User
import db

# Define a blueprint for configurations and set its prefix
config_bp = Blueprint('config', __name__, url_prefix='/configurations')

# Create a route for the configurations page
@config_bp.route('/', methods=['GET', 'POST'])
@login_required  # Restrict access to the page to authenticated users only
def config():
    if request.method == 'POST':  # If a POST request is received
        theme = request.form.get('theme')  # Get the selected theme from the request form
        db = current_app.config['db']  # Get the database object from the Flask application configuration
        with db.engine.begin() as conn:  # Open a connection to the database
            # Execute an UPDATE query to change the user's theme
            response = ("UPDATE users SET theme=? WHERE id=?", [theme, current_user.id])
            current_user.theme = theme  # Update the current user's theme in memory

    # Render the configurations page template with the current user's theme
    return render_template('config.html', theme=current_user.theme)
