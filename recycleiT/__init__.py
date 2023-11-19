import os

import psycopg2
from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
connect = psycopg2.connect(database='postgres', user='postgres', password='Goacamela4@',
                           host='localhost', port=5432)
cursor = connect.cursor()
app.config['SECRET_KEY'] = 'cc6bec6e43127bb74ea7b1fe'
