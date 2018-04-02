from flask import render_template

from todoApp import app

@app.route('/')

def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/todoApp')
def todoApp():
    user = {'username':'Wilson'}
    return  render_template('login.html',title='Login',user=user)