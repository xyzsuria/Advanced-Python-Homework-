import pymysql
conn=pymysql.connect(
    host="localhost",
    db="mycat",
    user="root",
    password="",
    charset="utf8"
)
#得到一个可以执行的SQL语句的光标对象
cursor=conn.cursor()
#sql="SELECT id,name,age from USER1 WHERE id=7;"#查询一条
sql="SELECT id,name,age from USER1;"#查询多条
cursor.execute(sql)
#ret=cursor.fetchone()#查询一条
ret=cursor.fetchall()#查询显示多条
cursor.close()
conn.close()
print(ret)