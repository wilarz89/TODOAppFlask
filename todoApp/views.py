from flask import render_template

from todoApp import app
from todoApp.forms import LoginForm

@app.route('/')

def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)