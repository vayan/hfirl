##
## hello.py for  in /home/vayan/hfirl
## 
## Made by yann vaillant
## Login   <vailla_y@epitech.net>
## 
## Started on  Wed Nov 23 12:56:30 2011 yann vaillant
## Last update Wed Nov 23 14:39:39 2011 florent espanet
##

from flask import Flask, request, redirect, render_template, url_for
from db import *

app = Flask(__name__)

@app.route('/')
def header():
    return render_template('index.html')

@app.route('/envoyer-un-haut-fait')
def submit():
    return render_template('submit.html')

@app.route('/ajout-hf', methods=['POST', 'GET'])
def add_hf():
    if request.method == 'POST':
        return request.form['hfname'] + request.form['hftext']
    return redirect(url_for('submit'))
if __name__ == '__main__':
    app.run(debug=True)

@app.route(’/users’)
def show_users():
    cur = g.db.execute(’select pseudo, rank from user order by id desc’)
    users = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_users.html', users=users)

