#Here we store the objects used in the app

from mongoengine import *
import  datetime


from flask_login import UserMixin

connect('todoflaskdb')


class User(UserMixin,Document):
    id = IntField(required=True)
    email = EmailField(required=True,max_length=50, unique=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    password = StringField(required=True,max_length=200)




STATUS = (('D','Done'),
          ('T','ToDo'))


class ToDoTasks(Document):
    id = IntField(required=True)
    description = StringField(required=True,max_length=500)
    dueDate = DateTimeField()
    dateCreated = DateTimeField(default= datetime.datetime.now)
    tags = ListField(StringField(max_length=30))
    active = StringField(max_length=2, choices=STATUS)
    timeWorked = DecimalField()
    user = ReferenceField(User,reverse_delete_rule=CASCADE)
    meta = {'allow_inheritance': True}

class DoneTasks(Document):
    id = IntField(required=True)
    description = StringField(required=True,max_length=500)
    dueDate = DateTimeField()
    dateCreated = DateTimeField(default= datetime.datetime.now)
    tags = ListField(StringField(max_length=30))
    active = StringField(max_length=2, choices=STATUS)
    timeWorked = DecimalField()
    user = ReferenceField(User,reverse_delete_rule=CASCADE)
    meta = {'allow_inheritance': True}











