import threading
import os
import requests
import re
from db import get_db

def sanitize_filename(filename):
    # Remove special characters from the filename
    return re.sub(r'[^\w\s-]', '', filename).strip()


def search_and_save_results():
    """ Get search term from the database and save to workspace"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT command_args FROM thoughts')
    search_term = cursor.fetchone()[0]

    # Build the search URL
    search_url = f"http://192.168.1.6:5000/search?q={search_term}"

    # Send the API request
    response = requests.get(search_url)

    # Check if the request was successful
    if response.status_code == 200:
        sanitized_filename = sanitize_filename(search_term)

        # Replace spaces with underscores in the sanitized filename
        sanitized_filename = re.sub(r'\s+', '_', sanitized_filename)

        # Save the response content to a file
        save_folder = os.path.join(os.getcwd(), 'workspace')
        save_filename = f"{sanitized_filename}.html"
        save_path = os.path.join(save_folder, save_filename)
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Search results saved successfully as {save_filename}.")
    else:
        print("Failed to retrieve search results.")

    db.close()
