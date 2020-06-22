# author: fanchuangwater@gmail.com
# date: 2020/6/21 下午7:08
# 目的: 

import os
from pathlib import Path

# CSRF_ENABLED 配置是为了激活 跨站点请求伪造 保护
CSRF_ENABLED = True

# 用来建立一个加密的令牌，用于验证一个表单。
SECRET_KEY = 'you-will-never-guess'

# Unix/Mac (note the four leading slashes)
# sqlite:////absolute/path/to/foo.db

# 下面 3 种写法都是可以的。
# SQLALCHEMY_DATABASE_URI = f'sqlite:////{os.getcwd()}/msg.db'
# SQLALCHEMY_DATABASE_URI = f'{__file__}/msg.db'
SQLALCHEMY_DATABASE_URI = f'sqlite:////{Path().resolve()}/msg.db'



