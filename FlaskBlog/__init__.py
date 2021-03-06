#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by jiar on 2016/12/27.
# Github: https://github.com/Jiar/

# from .config import DevConfig
# from flask import Flask, redirect, url_for

# app = Flask(__name__)
#
# # Get the config from object of DecConfig
# # 使用 onfig.from_object() 而不使用 app.config['DEBUG'] 是因为这样可以加载 class DevConfig 的配置变量集合，而不需要一项一项的添加和修改。
# app.config.from_object(DevConfig)
#
# from .controllers.blog import blog_blueprint
# app.register_blueprint(blog_blueprint)
# # app.register_blueprint(blog_blueprint, url_prefix='/blog')
# # app.register_blueprint(blog_blueprint, url_prefix='/blog', template_folder='templates/blog')
#
# @app.route('/')
# def index():
#     return redirect(url_for('blog.home'))
#
# if __name__ == '__main__':
#     # Entry the application
#     app.run(debug=True)

from flask import Flask, redirect, url_for

app = Flask(__name__)

from .models import db
from .controllers import blog, main
from .extensions import bcrypt

def create_app(object_name):
    """Create the app instance via `Factory Method`"""

    # Set the app config
    app.config.from_object(object_name)

    # Will be load the SQLALCHEMY_DATABASE_URL from config.py to db object
    db.init_app(app)

    # Init the Flask-Bcrypt via app object
    bcrypt.init_app(app)

    @app.route('/')
    def index():
        # Redirect the Request_url '/' to '/blog/'
        return redirect(url_for('blog.home'))

    # Register the Blueprint into app object
    app.register_blueprint(blog.blog_blueprint)
    app.register_blueprint(main.main_blueprint)

    return app
