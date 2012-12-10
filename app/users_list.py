from app import app, db, models, lm
from flask import render_template, flash, redirect, request, session, g, url_for
from flask.ext.login import login_user, logout_user, current_user, login_required

@app.route('/users_list')
def users_list():
    if g.user.is_authenticated():
        title = "Users List"
        users = models.User.query.all()
        return render_template(
            'users_list.html',
            users = users,
            title = title)
    else:
        return redirect(url_for('login'))
