from flask import render_template,json,url_for
from flask import flash,redirect,request,session,abort
from app import app
from mongoengine import *
from flask_login import current_user,login_user, logout_user
from app.models import User
import logging



@app.route('/')
def index():
    return render_template('login.html')


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    email = request.form['email']
    password = request.form['password']
    registered_user = User.objects(username=email, password=password).first()
    app.logger.info("enter ",registered_user)
    print(registered_user)
    if registered_user is None:
        flash('Username or Password is invalid', 'error')
        return render_template('login')
    login_user(registered_user)
    flash('Logged in successfully')
    return render_template('dashboard.html')


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/register-user',methods=['POST'])
def registeruser():
    user = User(
        email=request.form['email'],
        password_hash=request.form['password'],
        first_name=request.form['first_name'],
        last_name=request.form['last_name']
    )
    #user.set_password(request.form['password'])
    user.save()

    return render_template('login.html')