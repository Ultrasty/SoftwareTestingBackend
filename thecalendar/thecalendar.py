# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 21:22
# @Author  : STY
# @Email   : 1455670697@qq.com
# @File    : thecalendar.py
# @Software: PyCharm

import datetime


def calendar_atom(arg_list):
    v_list_new = [str(x) for x in arg_list]
    year, month, day = arg_list[0], arg_list[1], arg_list[2]
    if (year < 2000 or year > 2100) and (month < 1 or month > 12) and (day < 1 or day > 31):
        return 'Illegal Case'
    if year < 2000 or year > 2100:
        return 'Year Exceed'
    if month < 1 or month > 12:
        return 'Month Exceed'
    if day < 1 or day > 31:
        return 'Day Exceed'
    try:
        _date = datetime.datetime.strptime('-'.join(v_list_new), '%Y-%m-%d').date()
    except Exception as e:
        return str(e)
    return str(_date + datetime.timedelta(days=1))


if __name__ == '__main__':
    print(calendar_atom([2020, 12, 31]))
