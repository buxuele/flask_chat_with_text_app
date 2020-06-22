# author: fanchuangwater@gmail.com
# date: 2020/6/21 下午7:11
# 目的: 


# 以下来自官方文档
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class ChatForm(FlaskForm):
    msg_info = StringField('new_msg', validators=[DataRequired()])


