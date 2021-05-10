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


@app.route('/question2', methods=['POST', 'GET'])
def question2():
    file = request.files['file']
    file.save(os.getcwd() + '/' + file.filename)
    df = pd.read_csv(file.filename, sep=',', header=None)
    df[4] = 0
    df[5] = 0
    for i in range(df.shape[0]):
        df[4][i] = charges.compute(df[1][i], df[2][i])
        if df[3][i] != df[4][i]:
            df[5][i] = 0
        else:
            df[5][i] = 1

    da = json.dumps(df.to_dict(orient='records'))

    response = make_response(da)
    response.headers['Access-Control-Allow-Origin'] = "*"

    return response


if __name__ == '__main__':
    app.run()
