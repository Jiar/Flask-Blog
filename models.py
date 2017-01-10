#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by jiar on 2016/12/27.
# Github: https://github.com/Jiar/

from flask_sqlalchemy import SQLAlchemy
from main import app

# INIT the sqlalchemy object
# Will be load the SQLALCHEMY_DATABASE_URL from config.py
# SQLAlchemy 会自动的从 app 对象中的 DevConfig 中加载连接数据库的配置项
db = SQLAlchemy(app)

class User(db.Model):
    """Represents Proected users."""

    # Set the name for table
    __tablename__ = 'users'
    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    # Establish contact with Post's ForeignKey: user_id
    posts = db.relationship(
        'Post',
        backref='users',
        lazy='dynamic')

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        """Define the string format for instance of User."""
        return "<Model User `{}`>".format(self.username)

class Post(db.Model):
    """Represents Proected posts."""

    __tablename__ = 'posts'
    id = db.Column(db.String(45), promary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime)
    # Set the foreign key for Post
    user_id = db.Column(db.String(45), db.ForeignKey('users.id'))

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "<Model Post `{}`>".format(self.title)