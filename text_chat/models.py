# author: fanchuangwater@gmail.com
# date: 2020/6/21 下午8:28
# 目的: 

# 负责保存聊天信息的数据库

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from text_chat import app

db = SQLAlchemy(app)

"""
1. 支持的数据类型 
    https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
2. 
"""


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(100), unique=False, nullable=False)
    msg = db.Column(db.String(255), unique=False, nullable=False)
    send_time = db.Column(db.DateTime(), default=datetime.now)

    def __repr__(self):
        return f'{self.msg } from {self.sender} at: {str(self.send_time)}'

