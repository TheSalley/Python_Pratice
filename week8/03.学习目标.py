"""
数据的简单查询：
    无条件查询、字段的计算和字段的别名
数据的高级查询：
    数据排序、分页、去除重复记录
数据的有条件查询：
    条件表达式：数学运算符、比较运算符、逻辑运算符、按位运算符
"""

"""
数据表的基本查询：
    SELECT * FROM t_emp;
    SELECT empno, ename, sal FROM t_emp;

使用列别名：
    SELECT empno, sal * 12 AS "income" FROM t_emp;
    
数据分页：
    SELECT ... FROM ... LIMIT 起始位置,偏移量;
    SELECT empno, ename FROM t_emp LIMIT 0, 20;

结果集排序：
    SELECT ... FROM ... ORDER BY 列名 [ASC|DESC];
    可以写多个排序：
        SELECT ... FROM ... ORDER BY 列名 [ASC|DESC], 列名 [ASC|DESC];

排序 + 分页:
    ORDER BY 放在 LIMIT 前面

去重：
    SELECT DISTINCT 字段 FROM ...;
    使用DISTINCT 的SELECT 只能查询一列数据
"""