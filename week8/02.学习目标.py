"""
学习目标：
    1. 管理逻辑库和数据库
        创建、删除、修改逻辑库和数据库
    2. 了解常用的数据类型和约束
        字符串、整数、浮点数、日期、枚举、主键约束、非空约束、唯一约束、外键约束等
    3. 掌握索引机制和使用原则
        排序为什么可以提高数据检索速度？
        怎么创建和删除索引？
        什么条件下使用索引？
"""

"""
SQL 语言：是用于访问和处理数据的标准的计算机语言
分类：
    DML (数据)：
        添加、修改、删除、查询
    DCL (数据控制语言)：
        用户、权限、事务
    DDL (数据定义语言)：
        逻辑库、数据表、视图、索引
        
SQL 语句不区分大小写，但是字符串区分大小写；
SQL 语句必须以分号结尾；
SQL 语句的空格和换行是没有限制的；
# 这是注释
/* 这是注释 */ 
"""

"""
创建逻辑库：
    CREATE DATABASE 逻辑库名称;
查看所有逻辑库：
    SHOW DATABASES;
删除逻辑库：
    DROP DATABASE 逻辑库名称;
使用逻辑库:
    USE 逻辑库名称;
"""

"""
创建表：
    CREATE TABLE 数据表(
        列名1 数据类型 [约束] [COMMENT 注释],
        列名2 数据类型 [约束] [COMMENT 注释],
        ...
    )[COMMENT 注释];
插入数据：
    INSERT INTO student VALUES(
    1, 'faiz', '男', '1999-05-01', '13301111111', NULL
    );

修改表结构：
    添加字段：
        ALTER TABLE 表名称 
        ADD 列1 数据类型 [约束] [COMMENT 注释],
        ADD 列2 数据类型 [约束] [COMMENT 注释],
        ...;
    修改字段类型和约束
        ALTER TABLE 表名称
        MODIFY 列1 数据类型 [约束] [COMMENT 注释],
        MODIFY 列2 数据类型 [约束] [COMMENT 注释],
        ...;
    修改字段名称：
        ALTER TABLE 表名称：
        CHANGE 列1 新列名1 数据类型 [约束] [COMMENT 注释],
        CHANGE 列2 新列名2 数据类型 [约束] [COMMENT 注释],
        ...;
    删除字段：
        ALTER TABLE 表名称
        DROP 列1,
        DROP 列2,
        ...;

展示所有表：
    SHOW TABLES;
删除表:
    DROP TABLE student;
描述表：
    DESC student;
展示建表语句：
    SHOW CREATE TABLE student;
"""

"""
数据类型：
    数字：
        TINYINT 1byte 小整数
        SMALLINT 2byte 普通整数
        MEDIUMINT 3byte 普通整数
        INT 4byte 较大整数
        BIGINT 8byte 大整数
        FLOAT 4byte 单精度浮点数
        DOUBLE 8byte 双精度浮点数
        DECIMAL      DECIMAL(10, 2) 精确
    字符串：
        CHAR 1-255 固定长度
        VARCHAR 1-65535 不固定长度
        TEXT 1-65535 不确定长度
        MEDIUMTEXT 1-1千6百万 不确定长度
        LONGTEXT 1-42亿 不确定长度
    日期：
        DATE 3byte 日期
        TIME 3byte 时间
        YEAR 1byte 年份
        DATETIME 8byte 日期时间
        TIMESTAMP 4byte 时间戳
"""

"""
数据库的范式：
    构建数据库必须遵循一定的规则，这种规则就是范式
    目前，关系型数据库共有6 种范式：
        第一范式：
            原子性
            数据表的每一列都是不可分割的基本数据项，同一列中不能有多个值
        第二范式：
            唯一性
            数据表的每条记录必须是唯一的。通常要为数据表加上一个列来存储唯一标识
        第三范式：
            关联性
            每列都与主键有直接关系
"""

"""
字段约束：
    主键约束：
        PRIMARY KEY 字段值唯一，且不能为NULL
        建议主键一定要使用数字类型， 因为数字的检索速度会非常快
        如果主键是数字类型，可以设置为自动增长 AUTO_INCREMENT         
    非空约束：
        NOT NULL 字段值不能为NULL
        NOT NULL DEFAULT FALSE 
    唯一约束：
        UNIQUE 字段值唯一，且可以为NULL
    外键约束：
        FOREIGN KEY 保持关联数据的逻辑性
        外键约束的闭环问题：删除子表的记录必须先删除相关父表的
"""

"""
索引：
    加快数据查找速度
创建索引：
    CREATE TABLE 表名称(
    ...,
    INDEX [索引名称](字段),
    ...
    );
如何添加和删除索引：
    CREATE INDEX 索引名称 ON 表名(字段);
    ALTER TABLE 表名称 ADD INDEX [索引名称](字段);
    
    SHOW INDEX FROM 表名;
    
    DROP INDEX 索引名称 ON 表名;
"""
