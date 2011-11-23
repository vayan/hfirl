from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
<<<<<<< HEAD
def hello_world():
    return 'Hello World pd!'
=======
def header():
    return render_template('main.html')

@app.route('/caca')
def caca():
    return "caca"

@app.route('/caca/pipi')
def cacapipi():
    return "cacapipi"
>>>>>>> fbac063fb356425d6252182373bbe86e115a804f

if __name__ == '__main__':
    app.run(debug=True)
