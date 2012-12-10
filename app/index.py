from app import app, db, models, lm
from flask import render_template, flash, redirect, request, session, g, url_for
from flask.ext.login import login_user, logout_user, current_user, login_required
from forms import LoginForm

@app.before_request
def before_request():
    g.user = current_user

@lm.user_loader
def load_user(id):
    return models.User.query.get(int(id))

@app.route('/index', methods = ['GET', 'POST'])
@app.route('/', methods = ['GET', 'POST'])
def index():
    title = "Home"
    return render_template(
        'index.html',
        title = title)
