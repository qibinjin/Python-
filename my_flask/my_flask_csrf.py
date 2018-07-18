from flask import Flask, render_template, request, flash, make_response

from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField

from wtforms.validators import EqualTo, DataRequired
import os, base64
class Register(FlaskForm):
    username = StringField(label='用户名', validators=[DataRequired('用户名不能为空')], render_kw={'Placeholder':'请输入用户名'})
    password = PasswordField(label='密码', validators=[DataRequired('密码不能为空')])
    password2 = PasswordField(label='密码2', validators=[DataRequired('确认密码不能为空'), EqualTo('password','两次密码不一致')])
    submit = SubmitField(label='注册')

app = Flask(__name__)
app.secret_key='hdoijdwqoijdwqoijsalsaloiwqoijlsaldsal'
app.config['WTF_CSRF_ENABLED'] = False


def generate_csrf():
    return bytes.decode(base64.b64encode(os.urandom(48)))

@app.route('/', methods=['get', 'post'])
def index():
    form = Register()
    csrf_token = generate_csrf()
    if request.method == 'POST':
        csrf_token_form = request.form.get('csrf_token', '')
        csrf_token_cookie = request.cookies.get('csrf_token', '')
        print(csrf_token_form, csrf_token_cookie)
        if csrf_token_cookie != csrf_token_form:
            return '非法操作'

        if form.validate_on_submit():
            username = request.form.get('username', '')
            password = request.form.get('password', '')
            print(username, password)
            return 'success'
        else:
                flash(form.errors)
    response = make_response(render_template('login.html', form=form, csrf_token = csrf_token))
    response.set_cookie('csrf_token', csrf_token)

    return response




if __name__ == '__main__':

    app.run(debug=True)