from app import app, db, models
from flask import render_template, flash, redirect, request, session
from forms import LoginForm

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            username = form.username.data
            password = form.password.data
        except:
            print "foobar"
    return render_template(
        'index.html',
        form = form)
