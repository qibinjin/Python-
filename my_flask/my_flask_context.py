from flask import Flask, request, current_app, g, render_template
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

app.secret_key = 'aofirnjcspqoieqojdalkalq'


@app.route('/')
def index():
    g.name = 'user'
    abc = request.url + request.method + current_app.name + g.name
    return abc

@app.route('/user')
def user():
    my_list = [1,3,4,5]
    return render_template('base.html', list=my_list)

if __name__ == '__main__':
    manager.run()
