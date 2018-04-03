from flask import render_template
from flask import flash,redirect,request,session,abort
from app import app
from app.forms import LoginForm

@app.route('/')

def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Welcome!"

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return index()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return index()