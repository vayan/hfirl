from app import app, models, db
from flask import flash, redirect, url_for, g
from flask.ext.login import logout_user
from datetime import datetime

@app.route('/logout')
def logout():
    date_now = datetime.now().date()
    user = models.User.query.get(g.user.id)
    user.date_online = date_now
    db.session.commit()
    logout_user()
    return redirect(url_for('index'))
