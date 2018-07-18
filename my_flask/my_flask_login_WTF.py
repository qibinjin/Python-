from flask import Flask, render_template, flash, request

from flask_wtf import FlaskForm

from wtforms import SubmitField, StringField, PasswordField

from wtforms.validators import DataRequired, EqualTo


app = Flask(__name__)
app.secret_key = 'asdwfonoqnooqwedskmkqw'
app.config['WTF_CSRF_ENABLED'] = False

class RegisterForm(FlaskForm):
    username = StringField("用户名：", validators=[DataRequired("请输入用户名")], render_kw={"placeholder": "请输入用户名"})
    password = PasswordField("密码：", validators=[DataRequired("请输入密码")])
    password2 = PasswordField("确认密码：", validators=[DataRequired("请输入确认密码"), EqualTo("password", "两次密码不一致")])
    submit = SubmitField("注册")


@app.route('/', methods=['post', 'get'])
def index():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        print(username, password)
        return 'success'
    else:
        if request.method == 'POST':
            flash('参数有误或不完整')

    return render_template('login.html', form=register_form)

if __name__ == '__main__':

    app.run(debug=True)