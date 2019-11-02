import pymysql
conn=pymysql.connect(
    host="localhost",
    db="mycat",
    user="root",
    password="",
    charset="utf8"
)
cursor=conn.cursor()
ids=[3,5,6]#可以批量删除
sql="DELETE FROM USER1 WHERE id=%s;"
try:
    cursor.executemany(sql,ids)
    #提交事务
    conn.commit()
except Exception as e:
    conn.rollback()
cursor.close()
conn.close()