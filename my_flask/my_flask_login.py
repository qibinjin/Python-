from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'asddwbnoivsnohjoqoijdisa'

@app.route('/', methods=['post', 'get'])
def index():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        password2 = request.form.get('password2', '')

        if not all([username, password, password2]):
            flash('参数不足')
        elif password != password2:
            flash('两次密码不相同')
        else:
            print(username, password, password2)
            flash('注册成功')

    return render_template('login.html')

if __name__ == '__main__':

    app.run(debug=True)