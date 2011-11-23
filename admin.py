#!/usr/bin/python
# -*- coding: utf-8 -*-
##
## admin.py for firl in /home/volent/dev/hfirl
## 
## Made by florent espanet
## Login   <espane_f@epitech.net>
## 
## Started on  Wed Nov 23 12:56:22 2011 florent espanet
## Last update Wed Nov 23 14:32:13 2011 florent espanet
##

import sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, \
abort, render_template, flash

DATABASE = 'db/firl.db'
DEBUG = True
SECRET_KEY = 'we luvz python'
USERNAME = 'admin'
PASSWORD = 'admin'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('db/user.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
g.db = connect_db()
@app.teardown_request
def teardown_request(exception):
g.db.close()

@app.route(’/users’)
def show_users():
    cur = g.db.execute(’select pseudo, rank from user order by id desc’)
    users = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_users.html', users=users)

