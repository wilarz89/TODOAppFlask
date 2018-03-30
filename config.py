#basic configuration

# Enable Flask's debugging features. Should be False in production
DEBUG = True

#connect to database
from  mongoengine import *
connect('todoflaskdb')
