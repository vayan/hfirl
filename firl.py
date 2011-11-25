#!/usr/bin/python
# -*- coding: utf-8 -*-
## firl.py for  in /home/vayan/hfirl
##
## Made by yann vaillant
## Login   <vailla_y@epitech.net>
##
## Started on  Wed Nov 23 14:44:56 2011 yann vaillant
## Last update Fri Nov 25 13:36:15 2011 yann vaillant
##

import sqlite3
import time
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, \
abort, render_template, flash
from db import *

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

@app.route('/')
def header():
    return render_template('index.html')

@app.route('/ajouter-un-haut-fait')
def submit():
    return render_template('submit.html')

@app.route('/ajout-hf', methods=['POST', 'GET'])
def add_hf():
    if request.method == 'POST':
        g.db.execute('INSERT INTO hf (name, text) VALUES (?, ?)',
                     [request.form['hfname'], request.form['hftext']])
        g.db.commit()
    return redirect(url_for('submit'))

@app.route('/users')
def show_users():
    cur = g.db.execute('SELECT pseudo, rank FROM user ORDER BY id DESC')
    users = [dict(pseudo=row[0], rank=row[1]) for row in cur.fetchall()]
    return render_template('show_users.html', users=users)

@app.route('/add-user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        g.db.execute(' \
INSERT INTO user (pseudo, password, mail, avatar, rank, last_online) VALUES (?, ?, ?, " ", 1, ?)',\
[request.form['usrname'], request.form['usrpass'], request.form['usrmail'], int(time.time())])
    g.db.commit()
    return redirect(url_for('register'))

@app.route('/inscription')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
