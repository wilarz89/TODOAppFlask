#Here we store the objects used in the app
import datetime
from flask_mongoengine import MongoEngine
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash



db = MongoEngine('todoflaskdb')

class User(UserMixin,db.Document):
    id = db.IntField(required=True)
    email = db.StringField(required=True,max_length=50, unique=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    password = db.StringField(required=True,max_length=200)


class ToDoTasks(db.Document):
    id = db.IntField(required=True)
    description = db.StringField(required=True,max_length=500, unique=True)
    dueDate = db.DateTimeField()
    dateCreated = db.DateTimeField(default= datetime.datetime.now)
    tags = db.ListField(db.StringField(max_length=30))
    active = db.RadioField()
    timeWorked = db.DecimalField()

class DoneTasks(db.Document):
    id = db.IntField(required=True)
    description = db.StringField(required=True,max_length=500, unique=True)
    dueDate = db.DateTimeField()
    dateCreated = db.DateTimeField(default= datetime.datetime.now)
    tags = db.ListField(db.StringField(max_length=30))
    active = db.RadioField()
    timeWorked = db.DecimalField()







