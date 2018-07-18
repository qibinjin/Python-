from flask import Flask, redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


class RegConverter(BaseConverter):
    def __init__(self, url_map, regex):
        super(RegConverter, self).__init__(url_map)
        self.regex = regex

    def to_python(self, value):
        return value.split(',')

    def to_url(self, value):
        return ','.join([str(x) for x in value])


app.url_map.converters['rex'] = RegConverter


# class Config(object):
#     DEBUG=True
#
# app.config.from_object(Config)

# app.config.from_pyfile()

# IntegerConverter(self, url_map) == int
# RegConverter(self, url_map, r"(\d+,)+\d$")  == re(r"(\d+,)+\d$")



@app.route(r'/')
def index():
    return 'Hello World'


@app.route(r'/user/<rex(r"(\d+,)+\d$"):user_info>')
def user_info(user_info):
    return '%s' % user_info


@app.route(r'/demo1')
def demo1():
    return redirect(url_for('user_info', user_info=[1, 2, 3, 4]))

@app.before_first_request
def before_first_request():
    print('before_first_request')

@app.before_request
def before_request():
    print('before_request')


if __name__ == '__main__':
    app.run(debug=True)
