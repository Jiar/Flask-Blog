#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by jiar on 2016/12/27.
# Github: https://github.com/Jiar/

# from FlaskBlog import app, models
# from flask_migrate import Migrate, MigrateCommand
# from flask_script import Manager, Server
#
# # Init manager object via app object
# manager = Manager(app)
#
# # Init migrate object via app and db object
# # migrate = Migrate(app, models.db)
#
# # Create a new commands: server
# # This command will be run the Flask development_env server
# # manager.add_command("server", Server(host='127.0.0.1', port=8089))
# manager.add_command("server", Server())
# manager.add_command("db", MigrateCommand)
#
# @manager.shell
# def make_shell_context():
#     """Create a python CLI.
#
#     return: Default import object
#     type: `Dict`
#     """
#     # 确保有导入 Flask app object，否则启动的 CLI 上下文中仍然没有 app 对象
#     return dict(app=app,
#                 db=models.db,
#                 User=models.User,
#                 Post=models.Post,
#                 Comment=models.Comment,
#                 Tag=models.Tag,
#                 Posts_tags=models.posts_tags)
#
# if __name__ == '__main__':
#     manager.run()


import os

from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand

from FlaskBlog import create_app
from FlaskBlog import models


# Get the ENV from os_environ
env = os.environ.get('BLOG_ENV', 'dev')
# Create thr app instance via Factory Method
app = create_app('FlaskBlog.config.%sConfig' % env.capitalize())
# Init manager object via app object
manager = Manager(app)

# Init migrate object via app and db object
migrate = Migrate(app, models.db)

# Create some new commands
manager.add_command("server", Server(host='127.0.0.1', port=8089))
manager.add_command("db", MigrateCommand)


@manager.shell
def make_shell_context():
    """Create a python CLI.

    return: Default import object
    type: `Dict`
    """
    return dict(app=app,
                db=models.db,
                User=models.User,
                Post=models.Post,
                Comment=models.Comment,
                Tag=models.Tag,
                Server=Server)

if __name__ == '__main__':
    manager.run()