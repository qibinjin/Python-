from flask import Blueprint

users = Blueprint('user', __name__)

@users.route('/user/aa')
def user():
    return 'Hello World！'