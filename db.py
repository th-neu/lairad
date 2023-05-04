# Import necessary modules
import os
import sqlite3
import mariadb
from flask import g
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define function to get a database connection
def get_db(app):
    # Try to get the database connection from Flask's application context
    db = getattr(g, '_database', None)
    if db is None:
        # If no database connection exists, determine the type of database from environment variable DB_TYPE
        db_type = os.getenv('DB_TYPE')
        # If it is SQLite, get the database path from environment variable DATABASE and connect to it using sqlite3
        if db_type == 'sqlite':
            db_path = os.getenv('DATABASE')
            db = sqlite3.connect(db_path)
        # If it is MariaDB, get the credentials and connection details from environment variables and connect to it using mariadb
        elif db_type == 'mariadb':
            db_user = os.getenv('DB_USER')
            db_password = os.getenv('DB_PASSWORD')
            db_host = os.getenv('DB_HOST')
            db_port = os.getenv('DB_PORT')
            db_name = os.getenv('DB_NAME')
            db = mariadb.connect(
                user=db_user,
                password=db_password,
                host=db_host,
                port=int(db_port),
                database=db_name
            )
        # If an unsupported database type is specified in the environment variable, raise an error
        else:
            raise ValueError(f'Unsupported database type: {db_type}')
        # Save the database connection in Flask's application context
        g._database = db
        # Add the database connection to the app's config
        app.config['db'] = db
    return db

# Define function to close the database connection
def close_db(e=None):
    # Get the database connection from Flask's application context
    db = g.pop('_database', None)
    # If a database connection exists, close it
    if db is not None:
        db.close()
