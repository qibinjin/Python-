from flask import Flask, render_template, request, make_response
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    my_list = [1, 3, 4, 5]
    return render_template('index.html', list=my_list, username = request.cookies.get('username', ''))

@app.route('/user')
def user():
    my_list=[1,3,4,5]
    return render_template('base.html', list=my_list)

@app.route('/login')
def login():
    response = make_response('login success')
    response.set_cookie('username', 'laowang')

    return response

@app.route('/logout')
def logout():
    response=make_response('logout success')
    response.delete_cookie('username')
    return response


if __name__ == '__main__':
    manager.run()