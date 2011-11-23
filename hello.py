from import flask Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def header():
    return render_template('main.html')

@app.route('/caca')
def caca():
    return "caca"

@app.route('/caca/pipi')
def cacapipi():
    return "cacapipi"

if __name__ == '__main__':
    app.run(debug=True)
