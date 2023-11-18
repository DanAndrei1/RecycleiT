import psycopg2
from flask import Flask
from flask.cli import load_dotenv
import os

# from flask_login import LoginManager

app = Flask(__name__)
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'
# login_manager.login_message_category = 'info'
load_dotenv()
connect = psycopg2.connect(database=os.getenv('database'), user='postgres', password=os.getenv('password'),
                           host=os.getenv('host'), port=5432)
cursor = connect.cursor()
app.config['SECRET_KEY'] = os.getenv("secretkey")