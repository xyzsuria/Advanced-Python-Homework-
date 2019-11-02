import pymysql
conn=pymysql.connect(
    host="localhost",
    user="root",
    db="mycat",
    password="",
    charset="utf8"
)
#得到一个可以执行SQL的光标
cursor=conn.cursor()
sql="INSERT INTO USER1(name,age) VALUES (%s,%s);"
#u="Xu111"
#age=22#单个插入的例子
#批量插入
data=[("李紫瑶","19"),("严峫","30"),("江停","29")]
try:
    #插入数据库
    #cursor.execute(sql,[u,age])少量插入
    #批量插入
    cursor.executemany(sql,data)
    #提交事务
    conn.commit()
    #提交之后，获取刚插入的数据ID
    last_id=cursor.lastrowid
    #print(last_id)神奇，竟然真的能打出id
except Exception as e:
    #如有异常，回滚事务
    conn.rollback()
cursor.close()
conn.close()