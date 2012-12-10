from app import app, models, db
from flask import flash, redirect, url_for, g, render_template
from datetime import datetime

@app.route('/user/<username>')
def user(username):
    user = models.User.query.filter_by(username = username).first()
    if user == None:
        flash('User %s does not exist.' % (username,))
        return redirect(url_for('index'))
    return render_template(
        "user.html",
        user = user,
        title = username)
