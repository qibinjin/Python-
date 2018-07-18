from flask import Flask, render_template, flash, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os, base64

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost:3306/my_form_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = base64.b64encode(os.urandom(48))

db = SQLAlchemy(app)
migrations = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class MyForm(FlaskForm):
    author = StringField(label='作者:', validators=[DataRequired('请填写作者名')])
    book = StringField(label='书名:', validators=[DataRequired('请填写书名')])
    submit = SubmitField(label='添加')


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    books = db.relationship('Book', backref='author', lazy='dynamic')

    def __repr__(self):
        return 'Author: %s %s' % (self.name, self.id)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))


@app.route('/', methods=['POST', 'GET'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        author_name = request.form.get('author', '')
        book_name = request.form.get('book', '')
        try:
            author = Author.query.filter(Author.name == author_name).first()
            book = Book.query.filter(Book.name == book_name).first()
        except Exception as e:
            flash(e)
            return '插入出错'
        if not book:
            if author:
                try:
                    new_book = Book(name=book_name, author_id=author.id)
                    db.session.add(new_book)
                    db.session.commit()
                except Exception as e:
                    flash(e)
                    db.session.rollback()
            else:
                try:
                    new_author = Author(name=author_name)
                    db.session.add(new_author)
                    db.session.commit()
                    new_book = Book(name=book_name, author_id=new_author.id)
                    db.session.add(new_book)
                    db.session.commit()
                except Exception as e:
                    flash(e)
                    db.session.rollback()

        else:
            flash('此书已存在')
    else:
        if request.method == 'POST':
            flash(form.errors)

    authors = Author.query.all()
    return render_template('my_form.html', form=form, authors=authors)


@app.route('/delete_book')
def delete_book():
    id = request.args.get('id', '')
    try:
        book = Book.query.get(id)
    except Exception as e:
        flash(e)
        book = None

    if not book:
        flash('查无此书')
    else:
        try:
            db.session.delete(book)
            db.session.commit()
        except Exception as e:
            flash('删除失败，数据回滚')
            db.session.rollback()
    return redirect(url_for("index"))


@app.route('/delete_author')
def delete_author():
    id = request.args.get('id', '')
    try:
        author = Author.query.get(id)
    except Exception as e:
        flash(e)
        author = None

    if author:
        try:
            author.books.delete()
            db.session.delete(author)
            db.session.commit()
        except Exception as e:
            flash('删除失败,数据回滚')
            db.session.rollback()
    else:
        flash('查无此人')
    return redirect(url_for('index'))


if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    # au1 = Author(name='老王')
    # au2 = Author(name='老尹')
    # au3 = Author(name='老刘')
    # # 把数据提交给用户会话
    # db.session.add_all([au1, au2, au3])
    # # 提交会话
    # db.session.commit()
    # bk1 = Book(name='老王回忆录', author_id=au1.id)
    # bk2 = Book(name='我读书少，你别骗我', author_id=au1.id)
    # bk3 = Book(name='如何才能让自己更骚', author_id=au2.id)
    # bk4 = Book(name='怎样征服美丽少女', author_id=au3.id)
    # bk5 = Book(name='如何征服英俊少男', author_id=au3.id)
    # # 把数据提交给用户会话
    # db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    # # 提交会话
    # db.session.commit()

    manager.run()
