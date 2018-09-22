from app import app
from flask import render_template, flash, redirect, get_flashed_messages
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    return 'Hello, world!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    # 这个表格的地方有点意思，如果是post请求，那么这个form就是post请求提交的表格吗？
    # 那么如果是个get请求呢？
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        # 转换到一个新的网页上
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)


@app.route("/addflash")
def addFlash():
    flash("bling bling")
    flash("胡世昌是个大帅哥")
    return "added a flash"


@app.route("/getFlash/")
def getFlash():
    """
    这个get_flashed_messages返回的是上次请求里面的全部flash的信息
    :return:
    """
    msgs = get_flashed_messages()
    msgStr = ""
    for msg in msgs:
        msgStr += msg+","
    return msgStr