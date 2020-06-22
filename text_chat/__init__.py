# author: fanchuangwater@gmail.com
# date: 2020/6/21 下午6:41
# 目的: 


from flask import Flask

# 这一行必须写在上面，不然会出现包的导入错误。
app = Flask(__name__)
app.config.from_object('config')

# 这里的这一行必须写在下面
from text_chat import views

