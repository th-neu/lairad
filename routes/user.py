"""
module for adding a user
"""
from flask import Blueprint, render_template, request
from flask import redirect, url_for
from flask_login import login_required, current_user
from db import get_db
from models import User


user_bp = Blueprint('user', __name__, url_prefix='/')


@user_bp.route('/add_user', methods=['GET', 'POST'])
@login_required
def add_user(app=None):
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


@user_bp.route('/list_users')
@login_required
def list_users():
    """List all users"""
    user_objs = []
    users = User.get_all_users(user_objs)
    return render_template('list_users.html', users=users)


@user_bp.route('/delete_user/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    """Delete a user from the database"""
    # check if current user is admin
    if not current_user.is_admin:
        return redirect(url_for('home'))

    # Delete the user from the database
    conn = get_db()
    c = conn.cursor()
    c.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

    return redirect(url_for('user.list_users'))
