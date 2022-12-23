# coding:utf-8

import pymysql

conno = pymysql.connect(host='127.0.0.1',
                        port=8888,
                        user='root',
                        password='123456',
                        database='school',
                        charset='utf8mb4')

with conno.cursor() as cursor:
    cursor.execute(
        'select * from tb_student'
    )
    row = cursor.fetchall()
    for item in list(row):
        print(list(item)[1])


