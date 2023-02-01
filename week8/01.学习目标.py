"""
学习目标：
    1. 了解关系型数据库的诞生原因、优势
    2. MySQL 数据库的安装和初始化
    3. 学习管理MySQL 服务
    4. 创建新用户，并分配权限
    5. 了解MySQL 常用配置参数
"""

"""
数据库系统（DBMS）：是指一个能为用户提供信息服务的系统。
                它实现了有组织地、动态地存储大量相关数据的功能，
                提供了数据处理和信息资源共享的便利手段。
"""

"""
关系型数据库系统（RDBMS）：是指采用了关系模型的数据库系统。
                        关系模型中，数据是分类存放的，数据之间可以有联系。
                        主流的关系型数据库: Oracle、MySQL、SQL Server、DB2
"""

"""
NoSQL 数据库：指的是数据分类存放，但是数据之间没有关联关系的数据库系统。
            主流的NoSQL 数据库：Redis、MongoDB、MenCache、Neo4J
"""

"""
cmd 命令连接mysql：mysql -u root -p
"""
# mysql 的用户管理

"""
创建数据库 CREATE DATABASE test;
修改root密码 ALTER USER 'root'@'localhost' IDENTIFIED BY '123456'; 存到记事本
            管理员打开cmd mysqld --defaults-file="C:\MySQL Server 8.0\my.ini" --init-file="E:\temp.txt" --console
停止mysql服务 net stop mysql80
启动mysql服务 net start mysql80
"""

"""
mysql 配置文件:
    my.ini 文件中，我们可以设置各种mysql 的配置，如字符集、端口号等
        客户端配置信息：[client]、[mysql]
        数据库配置信息：[mysqld]
"""