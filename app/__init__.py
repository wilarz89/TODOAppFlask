from flask import Flask
from config import  Config


# Initialize the app
app = Flask(__name__)



# Load the config file
app.config.from_object(Config)

# Load the views
from app import views

