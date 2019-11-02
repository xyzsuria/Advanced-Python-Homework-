import pymysql
conn=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="mycat",
    charset="utf8"
)
#得到一个可以执行SQL语句的光标对象
cursor=conn.cursor()
sql="""
CREATE TABLE USER1(
    id INT auto_increment PRIMARY KEY,
    name CHAR(10) NOT NULL UNIQUE,
    age TINYINT NOT NULL
)ENGINE=innodb DEFAULT CHARSET=utf8;
"""
#执行SQL语句
cursor.execute(sql)
#关闭光标
cursor.close()
#关闭数据库
conn.close()
#结果是在mycat数据库中创建了一个user1表