"""
add prompt route / list / add
"""

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from db import get_db
from models import Prompts

prompt_bp = Blueprint('prompt', __name__, url_prefix='/')


@prompt_bp.route('/add_prompt', methods=['GET', 'POST'])
@login_required
def add_project(app=None):
    """Define a route for adding a project to the database"""
    # check if current user is admin
    if not current_user.is_admin:
        return redirect(url_for('home'))

    if request.method == 'POST':
        # Get the project details from the form
        project_name = request.form['project_name']
        project_desc = request.form['project_desc']
        project_goal = request.form['project_goal']

        # Save the project details to the database
        conn = get_db(app)
        c = conn.cursor()
        c.execute(
            'INSERT INTO projects (name, description, goals)'
            'VALUES (?, ?, ?)',
            (project_name, project_desc, project_goal))
        conn.commit()
        conn.close()

        return redirect(url_for('home'))

    # Render the add user form
    return render_template('add_prompt.html')


@prompt_bp.route('/list_prompts')
@login_required
def list_prompts():
    """List all projets"""
    prompt_objs = []
    prompts = Prompts.get_all_prompts(prompt_objs)
    return render_template('list_prompts.html', prompts=prompts)


@prompt_bp.route('/delete_prompt/<int:prompt_id>', methods=['POST'])
@login_required
def delete_project(prompt_id):
    """Delete a project from the database"""
    # check if current user is admin
    if not current_user.is_admin:
        return redirect(url_for('home'))

    # Delete the project from the database
    conn = get_db()
    c = conn.cursor()
    c.execute('DELETE FROM projects WHERE id = ?', (prompt_id,))
    conn.commit()
    conn.close()

    return redirect(url_for('prompt.list_prompts'))
