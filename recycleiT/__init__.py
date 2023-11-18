import os
import psycopg2
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# load_dotenv()
connect = psycopg2.connect(database=os.getenv('database'), user=os.getenv('user'), password=os.getenv('password'),
                           host=os.getenv('host'), port=os.getenv('port'))
