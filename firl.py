##
## hello.py for  in /home/vayan/hfirl
## 
## Made by yann vaillant
## Login   <vailla_y@epitech.net>
## 
## Started on  Wed Nov 23 12:56:30 2011 yann vaillant
## Last update Wed Nov 23 14:20:12 2011 yann vaillant
##

from flask import Flask, request, redirect, render_template, url_for

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
