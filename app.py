# -*- coding: utf-8 -*-
# @Time    : 2021/5/10 18:28
# @Author  : STY
# @Email   : 1455670697@qq.com
# @File    : app.py
# @Software: PyCharm

from flask import Flask, make_response
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


@app.route('/question2', methods=['OPTIONS'])
def question2o():
    response = make_response()
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Allow'] = "HEAD, POST, OPTIONS, GET"
    a = request
    print(a)
    return response


@app.route('/question2', methods=['POST', 'GET'])
def question2():
    response = make_response()
    response.headers['Access-Control-Allow-Origin'] = "*"
    a = request
    print(a.files['file'].filename)
    return response


if __name__ == '__main__':
    app.run()
