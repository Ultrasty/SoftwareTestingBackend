# -*- coding: utf-8 -*-
# @Time    : 2021/5/10 18:28
# @Author  : STY
# @Email   : 1455670697@qq.com
# @File    : app.py
# @Software: PyCharm
import json
import os
from flask import Flask, make_response, request, redirect, url_for, send_from_directory
import pandas as pd
import charges.charges as charges
import computer.computer as computer

app = Flask(__name__)


@app.route('/question2', methods=['OPTIONS'])
def question2o():
    response = make_response()
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Allow'] = "HEAD, POST, OPTIONS, GET"
    a = request
    print(a)
    return response


@app.route('/question3', methods=['OPTIONS'])
def question3o():
    response = make_response()
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Allow'] = "HEAD, POST, OPTIONS, GET"
    a = request
    print(a)
    return response


@app.route('/question2', methods=['POST', 'GET'])
def question2():
    file = request.files['file']
    file.save(os.getcwd() + '/' + file.filename)
    df = pd.read_csv(file.filename, sep=',', header=None)
    df[4] = 0
    df[5] = 0
    for i in range(df.shape[0]):
        df.loc[i, 4] = charges.compute(df[1][i], df[2][i])
        if str(df[3][i]) != str(df[4][i]):
            df.loc[i, 5] = "未通过测试"
        else:
            df.loc[i, 5] = "通过测试"

    da = json.dumps(df.to_dict(orient='records'))

    response = make_response(da)
    response.headers['Access-Control-Allow-Origin'] = "*"

    return response


@app.route('/question3', methods=['POST', 'GET'])
def question3():
    file = request.files['file']
    file.save(os.getcwd() + '/' + file.filename)
    df = pd.read_csv(file.filename, sep=',', header=None)
    df[5] = 0
    df[6] = 0
    for i in range(df.shape[0]):
        df.loc[i, 5] = computer.compute(df[1][i], df[2][i], df[3][i])
        if str(df[4][i]) != str(df[5][i]):
            df.loc[i, 6] = "未通过测试"
        else:
            df.loc[i, 6] = "通过测试"

    da = json.dumps(df.to_dict(orient='records'))

    response = make_response(da)
    response.headers['Access-Control-Allow-Origin'] = "*"

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')
