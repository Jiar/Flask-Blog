#!/usr/bin/env python3
# -*- coding= utf-8 -*-

# Created by jiar on 2017/1/11.
# Github: https://github.com/Jiar/

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class CommentForm(Form):
    """Form vaildator for comment."""

    # Set some field(InputBox) for enter the data.
    # patam validators: setup list of validators
    name = StringField(
        'Name',
        validators=[DataRequired(), Length(max=255)])

    text = StringField(u'Comment', validators=[DataRequired()])