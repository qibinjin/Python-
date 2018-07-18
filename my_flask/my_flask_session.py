from flask import Flask, session
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

app.secret_key='aofirnjcspqoieqojdalkalq'

@app.route('/')
def index():
    username = session.get('username', '')
    return 'hello world %s ' % username

@app.route('/login')
def login():

    session['username'] = 'laowang'
    return 'login success'

@app.route('/logout')
def logout():
    session.pop('username', None)
    return 'logout success'




if __name__ == '__main__':

    manager.run()