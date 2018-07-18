from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost:3306/my_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    __tablename__ =  'articles'

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(64))
    title = db.Column(db.String(64))
    detail = db.Column(db.Text)
    time = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    def __repr__(self):
        return 'articles %s %s' % (self.title, self.author)


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    author_img = db.Column(db.String(64), nullable=True)
    author_name = db.Column(db.String(64))
    author_resume = db.Column(db.String(64))
    writings = db.Column(db.Integer)
    follows = db.Column(db.Integer)
    articles = db.relationship('Article', backref='author')

    def __repr__(self):
        return 'authors %s %s ' % (self.name, self.writings)


class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.Text)
    comment_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return 'comment %s %s' % (self.comment_text, self.comment_time)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_pic = db.Column(db.String(64))
    user_name = db.Column(db.String(64))
    comments = db.relationship('Comments', backref='user')

    def __repr__(self):
        return 'user %s' % self.user_name


@app.route('/')
def index():
    artilce_list = Article.query.all()

    return render_template('index.html', artilce_list=artilce_list)


@app.route('/detail')
def detail():
    id = request.args.get('id', '')
    comments_list = Comments.query.all()
    article = Article.query.get(id)
    author = article.author
    return render_template('detail.html', comments_list=comments_list, author=author)


if __name__ == '__main__':
    # model.db.drop_all()
    # model.db.create_all()
    #
    # author1 = model.Author(author_img='../static/images/user_pic.png', author_name='张大山', author_resume='张大山的简介,张大山',
    #                        writings=23, follows=36)
    # user1 = model.User(user_pic = '../static/images/worm.jpg', user_name = '张山')
    # model.db.session.add_all([author1, user1])
    # model.db.session.commit()
    #
    # article1 = model.Article(image='../static/images/news_pic.jpg', title='日本史上最大IPO之一要来了：软银计划将手机业务分拆上市软银计划将手机业务分拆上市', detail='据日经新闻网，软银计划让旗下核心业务移动手机部门SoftBank Corp.分拆上市，或募资2万亿日元(约180亿美元)。随着软银逐步向投资公司转型，此举旨在给手机业务部门更多自主权。',
    #                          time='2017-01-01 00:00:00', author_id = author1.id)
    #
    # comment1 = model.Comments(comment_text = '遏制茅台酒价格过快上涨，多渠道供给，就不一定要买，租茅台酒也可以的，租售同权。开发共有产权茅台酒，让老百姓喝得起茅台酒，饮者有其酒。',
    #                           comment_time = '2017-01-01 00:00:00', user_id = user1.id)
    #
    # model.db.session.add_all([article1, comment1])
    # model.db.session.commit()
    app.run(debug=True)
