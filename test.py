# -*- coding: utf-8 -*-
__author__ = 'rsj217'

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import time

app = Flask(__name__)

# config.py
# dialect+driver://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/dev_db?charset=utf8'

db = SQLAlchemy(app)

# models
class User(db.Model):
    """ 用户模型定义了三个字段， 数据库表名为model名小写
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

    def save(self):
        db.session.add(self)
        db.session.commit()


class Category(db.Model):
    """ 栏目模型，与文章是一对多关系，自身是一对一关系
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    # 父栏目id
    pid = db.Column(db.Integer, db.ForeignKey('category.id'))
    # 父栏目对象
    pcategory = db.relationship('Category', uselist=False, remote_side=[id], backref=db.backref('scategory', uselist=False))

    def __init__(self, name, pcategory=None):
        self.name = name
        self.pcategory = pcategory

    def __repr__(self):
        return '<Category %r>' % self.name

    def save(self):
        db.session.add(self)
        db.session.commit()

# 多对多中间表
post_tag = db.Table('post_tag',
                    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                )


class Post(db.Model):
    """ 文章模型，与栏目是多对一关系，与标签是多对多关系
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.String(20))
    # 所属栏目id
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    # 所属栏目对象，外键对象，不会生成数据库实际字段
    # backref指反向引用，也就是外键Category通过backref(post_set)查询Post
    category = db.relationship('Category', backref=db.backref('post_set', lazy='dynamic'))

    tags = db.relationship('Tag', secondary=post_tag,
                           backref=db.backref('post_set', lazy='dynamic'))

    def __init__(self, title, body, category, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = time.time()
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title

    def save(self):
        db.session.add(self)
        db.session.commit()

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(10), unique=True)

    posts = db.relationship('Post', secondary=post_tag,
                            backref=db.backref('tag_set', lazy='dynamic'))

    def __init__(self, content):
        self.content = content

    def save(self):
        db.session.add(self)
        db.session.commit()

def main():
    db.create_all()
    app.run()

if __name__ == '__main__':
    main()