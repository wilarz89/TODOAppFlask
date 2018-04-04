#Here we store the objects used in the app

from mongoengine import *
import datetime


from flask_login import UserMixin
from app import login
from werkzeug.security import generate_password_hash,check_password_hash

connect('todoflaskdb')

# all user models and database interactions
class User(UserMixin,Document):
    email = EmailField(required=True,max_length=50, unique=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    password_hash = StringField(required=True,max_length=200)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.objects(pk=id).first()

STATUS = (('D','Done'),
          ('T','ToDo'))


class ToDoTasks(Document):
    description = StringField(required=True,max_length=500)
    dueDate = DateTimeField()
    dateCreated = DateTimeField(default= datetime.datetime.now)
    tags = ListField(StringField(max_length=30))
    active = StringField(max_length=2, choices=STATUS)
    timeWorked = DecimalField()
    user = ReferenceField(User,reverse_delete_rule=CASCADE)
    meta = {'allow_inheritance': True}

class DoneTasks(Document):
    description = StringField(required=True,max_length=500)
    dueDate = DateTimeField()
    dateCreated = DateTimeField(default= datetime.datetime.now)
    tags = ListField(StringField(max_length=30))
    active = StringField(max_length=2, choices=STATUS)
    timeWorked = DecimalField()
    user = ReferenceField(User,reverse_delete_rule=CASCADE)
    meta = {'allow_inheritance': True}











