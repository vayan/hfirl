from app import app
from flask import flash, redirect, url_for
from flask.ext.login import logout_user

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
