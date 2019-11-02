import pymysql
conn=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    charset="utf8",
    db="mycat"
)
cursor=conn.cursor()
sql="UPDATE USER1 SET age=%s WHERE name=%s;"
#uname="李紫瑶"
#age=20#单个插入
#批量的话改的内容在前面
datas=[(19,"李紫瑶"),(28,"江停")]
try:
    cursor.executemany(sql,datas)#批量修改
    conn.commit()
except Exception as e:
    conn.rollback()
cursor.close()
conn.close()