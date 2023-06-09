"""
module to change the theme *not working*
"""
# Import necessary modules
from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
# from models import User
from db import get_db


theme_bp = Blueprint('theme', __name__, url_prefix='/theme')
"""Define a blueprint for configurations and set its prefix"""


@theme_bp.route('/', methods=['GET', 'POST'])
@login_required  # Restrict access to the page to authenticated users only
def theme(app=None):
    """Create a route for the configurations page"""
    if request.method == 'POST':  # If a POST request is received
        theme = request.form.get('theme')
        conn = get_db(app)
        c = conn.cursor()
        c.execute(
                "UPDATE users SET theme=? WHERE id=?",
                [theme, current_user.id])
        current_user.theme = theme
        conn.commit()
        conn.close()

    # Render the configurations page template with the current user's theme
    return render_template('theme.html', theme=current_user.theme)
