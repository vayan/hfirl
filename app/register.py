from app import app, db, models
from flask import render_template, flash, redirect, request, session, url_for
from forms import RegisterForm
import re

def valid_email(email):
    result = re.match("^[a-zA-Z0-9._%-+]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}$", email)
    if result == None:
        flash('Your email is not valid.')
        return False
    else:
        return True

def user_exist(username, email):
    users = models.User.query.all()
    for u in users:
        if u.username == username:
            flash('User %s already exists.' % username)
            return True
        elif u.email == email:
            flash('Your email is already in use.')
            return True
    return False

def valid_password(password):
    if not len(password) >= 6:
        flash('Password is too short (minimum 6 characters).')
        return False
    return True

def add_user(username, password, email):
    if not valid_email(email):
        return False
    if user_exist(username, email):
        return False
    if not valid_password(password):
        return False
    user = models.User(username = username, password = password, email = email)
    db.session.add(user)
    db.session.commit()
    flash('Signing in successfull !' % user)
    return True

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        if add_user(username, password, email):
            return redirect(url_for('index'))
        else:
            return redirect(url_for('register'))
    return render_template(
        'register.html',
        form = form)
