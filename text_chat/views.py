# author: fanchuangwater@gmail.com
# date: 2020/6/21 下午6:41
# 目的: 

# local packages
from text_chat import app
from text_chat.models import db, Message
from text_chat.forms import ChatForm

from flask import render_template, redirect, url_for
from flask import request


@app.route('/')
@app.route('/index', methods=('GET', "POST"))
def home():
    # return "你是最棒的！"
    # user = {'nickname': "唐晖"}
    ip = request.remote_addr
    headers = request.headers
    x = headers["User-Agent"]
    # print(x)
    # Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36
    user = ip + ": " + x   # 这样的话，使用２个浏览器来假装成２个用户俩进行交流了。

    msgs = Message.query.all()
    form = ChatForm()

    if request.method == 'POST' and form.validate_on_submit():
        a_msg = form.msg_info.data
        db.session.add(Message(sender=user, msg=a_msg))
        db.session.commit()     # 这个不要忘了。
        return redirect(url_for("home"))

    return render_template("home.html",
                           title="文字通话",
                           msgs=msgs,
                           form=form,
                           ip=ip,
                           headers=headers,
                           )

@app.route('/')
def update_chat_status():
    pass
    #



@app.route("/success")
def nice():
    return "this message is valid!"
