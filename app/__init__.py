from flask import Flask
from config import  Config
from flask_login import LoginManager

# Initialize the app
app = Flask(__name__)

login = LoginManager(app)
login.login_view = 'login'
# Load the config file
app.config.from_object(Config)

# Load the views
from app import views

