from flask import render_template,json,url_for
from flask import flash,redirect,request,session,abort
from app import app
from mongoengine import *
from flask_login import current_user,login_user, logout_user
from app.models import User

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated ==True:
        return redirect(url_for('dashboard'))
    form = request.form
    if form.validate_on_submit():
        user = User.objects(username=form.username).first()
        if user is None or not user.check_password(form.password):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me)
        return redirect(url_for('index'))
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
        first_name=request.form['first_name'],
        last_name=request.form['last_name']
    )
    user.set_password(request.form['password'])
    user.save()

    return render_template('login.html')