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

api_url = os.getenv("LLAMA_CCP_API_URL")
llama_temperature = os.getenv("LLAMA_TEMPERATURE")
llama_tokens = os.getenv("LLAMA_MAX_TOKEN")
llama_echo = os.getenv("LLAMA_ECHO")
llama_request_timeout = int(os.getenv("LLAMA_REQUEST_TIMEOUT"))


def llama_cpp_python_api():
    with current_app.app_context():
        # Read the prompt text from the database or any other source
        prompt = Prompts.get_prompt_from_database()

        # Request body
        data = {
            "temperature": llama_temperature,
            "max_tokens": llama_tokens,
            "stop": ["###"],
            "prompt": prompt
        }

        # Send the POST request to the API
        try:
            response = requests.post(
                                    api_url,
                                    json=data,
                                    timeout=llama_request_timeout
                                    )
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while sending the request: {e}")
            exit(1)

        # Process the response or perform any other actions
        # response_data = response.json()
        # ...
        # Implement your response processing logic here

        # You can return a result or update the database if needed
        # ...


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


@worker_bp.route('/select_project', methods=['GET', 'POST'])
@login_required
def select_project():
    """select project route"""
    if request.method == 'POST':
        # get the selected project from the form
        project_id = request.form.get('project_id')
        task = Projects.get_task_from_database()
        p = start_worker(task, llama_cpp_python_api)
        worker_processes.append(p)
        return 'Worker started'
    else:
        # get all projects from the database
        projects = Projects.get_all_projects()
        return render_template('select_project.html', projects=projects)
