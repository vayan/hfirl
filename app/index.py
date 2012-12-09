from app import app, db, models, lm
from flask import render_template, flash, redirect, request, session, g, url_for
from flask.ext.login import login_user, logout_user, current_user, login_required
from forms import LoginForm

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.before_request
def before_request():
    g.user = current_user

@lm.user_loader
def load_user(id):
    return models.User.query.get(int(id))

def user_can_login(username, password):
    if not (g.user is not None and g.user.is_authenticated()):
        user = models.User.query.filter_by(username = username).first()
        try:
            if user.username == username and user.password == password:
                return user
        except:
            pass
    return False

@app.route('/index', methods = ['GET', 'POST'])
@app.route('/', methods = ['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = user_can_login(username, password)
        if user:
            login_user(user, remember = False)
            return redirect(url_for('index'))
    return render_template(
        'index.html',
        form = form)
