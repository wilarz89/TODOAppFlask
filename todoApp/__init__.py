from flask import Flask
from flask_mongoengine import MongoEngine

# Initialize the app
app = Flask(__name__, instance_relative_config=True)
app.config["MONGODB_SETTINGS"] = {"DB": "localhost:27017"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)

# Load the views
from todoApp import  views

# Load the config file
app.config.from_object('config')