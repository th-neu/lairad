from flask import Blueprint, render_template, request, redirect, url_for, current_app
# from flask import current_app as app
from flask_login import login_required, current_user
from db import get_db


user_bp = Blueprint('user', __name__, url_prefix='/')


@user_bp.route('/add_user', methods=['GET', 'POST'])
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