from app import app, db, models, lm
from flask import render_template, flash, redirect, request, session, g, url_for
from flask.ext.login import login_user, logout_user, current_user, login_required
from forms import LoginForm

def user_can_login(username, password):
    if not (g.user is not None and g.user.is_authenticated()):
        user = models.User.query.filter_by(username = username).first()
        try:
            if user.username == username and user.password == password:
                return user
        except:
            pass
    return False

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    title = "Login"
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = user_can_login(username, password)
        print user
        if user:
            login_user(user, remember = True)
            return redirect(url_for('index'))
    return render_template(
        'login.html',
        title = title,
        form = form)
