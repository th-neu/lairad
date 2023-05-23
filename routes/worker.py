"""
worker start/stop
"""
import os
import requests
# import re
from flask import Blueprint, render_template
from flask import request, redirect, url_for, current_app
from flask_login import login_required
from dotenv import load_dotenv
from worker_manager import start_worker, stop_worker
from models import Projects, Prompts

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')

load_dotenv(dotenv_path)

worker_bp = Blueprint('worker', __name__, url_prefix='/')

worker_processes = []  # Define the worker_processes list


@worker_bp.route('/start_worker/<int:project_id>')
@login_required
def start_worker_route(project_id):
    """start worker route"""
    project = Projects.query.first()  # Get the first project from the database
    task = {'api_url': 'https://example.com/api', 'data': {'project_id': project.id}}
    # task = Projects.get_task_from_database()
    p = start_worker(llama_cpp_python_api)
    worker_processes.append(p)
    return 'Worker started'


@worker_bp.route('/stop_worker')
@login_required
def stop_worker_route():
    """stop_worker route"""
    if len(worker_processes) > 0:
        p = worker_processes.pop()
        stop_worker(p)
        return 'Worker stopped'
    return 'No worker processes to stop'


@worker_bp.route('/start_worker', methods=['POST'])
@login_required
def start_worker_form():
    project_id = request.form['project']
    return redirect(url_for('worker.start_worker_route', project_id=project_id))
