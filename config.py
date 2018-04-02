#basic configuration
import os

# Enable Flask's debugging features. Should be False in production
DEBUG = True

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-is-a-secret-key'


