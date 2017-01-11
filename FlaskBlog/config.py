#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by jiar on 2016/12/27.
# Github: https://github.com/Jiar/

class Config(object):
    """Base config class."""
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'www.jiar.vip|www.jiar.vip'

class ProdConfig(Config):
    """Production config class."""
    pass

class DevConfig(Config):
    """Development config class."""
    # Open the DEBUG
    DEBUG = True
    # MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:664198@127.0.0.1:3306/Flask-Blog'
