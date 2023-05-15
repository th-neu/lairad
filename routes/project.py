"""
add projects route / list
"""

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from db import get_db
from models import Projects

project_bp = Blueprint('project', __name__, url_prefix='/')


@project_bp.route('/add_project', methods=['GET', 'POST'])
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
    return render_template('add_project.html')


@project_bp.route('/list_projects')
@login_required
def list_projects():
    """List all projets"""
    project_objs = []
    projects = Projects.get_all_projects(project_objs)
    return render_template('list_projects.html', projects=projects)


@project_bp.route('/delete_project/<int:project_id>', methods=['POST'])
@login_required
def delete_project(project_id):
    """Delete a project from the database"""
    # check if current user is admin
    if not current_user.is_admin:
        return redirect(url_for('home'))

    # Delete the project from the database
    conn = get_db()
    c = conn.cursor()
    c.execute('DELETE FROM projects WHERE id = ?', (project_id,))
    conn.commit()
    conn.close()

    return redirect(url_for('project.list_projects'))
