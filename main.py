from flask import flask
from datetime import datetime
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s !' % name

@app.route('/bye/<name>')
def bye_name(name):
    return 'Bye %s !' % name

@app.route('/hello_with_datetime/<name>')
def hello_name(name):
   return f'Hello{name}! Thank You for checking out at {datetime.now()}'

@app.route('/bye_with_datetime/<name>')
def bye_with_datetime(name):
   return f'bye{name}! cuurent time at {datetime.now()}'

    if __name__ == '__main__':
        app.run()
