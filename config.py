import os,jinja2
# Statement for enabling the development environment
DEBUG = True

# Define the application directory

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"


# TEMPLATES FOLDER
TEMPLATE_FOLDER = "templates"


# JINJA LOADER
JINJA_ENVIRONMENT = jinja2.ChoiceLoader([
    jinja2.FileSystemLoader([x[0] for x in os.walk('templates')]),
])

# ASSETS FOLDER
ASSETS_FOLDER = "templates"

# Define the database - we are working with

# MONGODB CONFIGURATION
MONGO_HOST='localhost'
MONGO_PORT=27017
MONGO_DBNAME='todoflaskdb'