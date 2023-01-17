# coding:utf-8

import pymysql

# 建立数据库连接
db = pymysql.connect(host='127.0.0.1',
                     port=8888,
                     user='root',
                     password='123456',
                     database='movie',
                     charset='utf8mb4')
# 创建游标对象
cursor = db.cursor()
# execute() 执行SQL 语句
cursor.execute(
    'DROP TABLE IF EXISTS all_movies'
)
# 创建表
sql = """
    CREATE TABLE all_movies (
        id int NOT NULL AUTO_INCREMENT,
        title varchar(100) NOT NULL,
        score float,
        comment varchar(255),
        PRIMARY KEY (id)
    )
"""

cursor.execute(sql)

sql = """
    INSERT INTO all_movies(
        title, score, comment
    )VALUES ('肖申克的救赎', 9.7, '希望让人自由。'  )
"""

cursor.execute(sql)
db.commit()

# fetchall() 获取所有数据
# data = cursor.fetchone()

# print(data)

# 关闭数据库连接
db.close()
