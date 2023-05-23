"""
database access
"""
import os
import sqlite3
import mariadb
from flask import g, Flask
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()


def get_db():
    """get db"""
    db = getattr(g, '_database', None)
    if db is None:
        db_type = os.getenv('DB_TYPE')
        if db_type == 'sqlite':
            db_path = os.getenv('DATABASE')
            db = sqlite3.connect(db_path)
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
        else:
            raise ValueError(f'Unsupported database type: {db_type}')
        g._database = db
    return db


def close_db():
    """close db"""
    db = g.pop('_database', None)
    if db is not None:
        db.close()
