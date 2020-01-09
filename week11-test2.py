import os
import json
import pymysql

conn=pymysql.connect(
    host="localhost",
    user="root",
    db="KeKe",
    password="",
    charset="utf8"
)
cursor = conn.cursor()

def EndConn():
    cursor.close()
    conn.close()

sql="""
    CREATE TABLE KE(
    id INT auto_increment PRIMARY KEY,
    title CHAR(50),
    author CHAR(10),
    time CHAR(20),
    info CHAR(50),
    zh CHAR(255),
    en CHAR(255)
    )ENGINE=innodb DEFAULT CHARSET=utf8;
"""
try:
    cursor.execute(sql)
    EndConn()
except Exception as e:
    print("数据库已存在！")


def AddMysql(content): 
    sql = "INSERT INTO KE(title,author,time,info,zh,en) VALUES(%s,%s,%s,%s,%s,%s);"
    try:
        cursor.execute(sql,[content["title"],content["author"],content["time"],content["info"],content["zh"],content["en"]])
        conn.commit()
    except Exception as e:
        conn.rollback()
    # conn.ping(reconnect=True)


def KeKeInsert(KeKeList):
    for i in KeKeList:
        AddMysql(i)
    EndConn()


os.chdir(r'.\sort')
r = open('text.txt','r')
f = r.read()
r.close()
# json.loads()的功能是讲字符串转为字典
x = json.loads(f) # x是一个列表
KeKeInsert(x)
# content = x[0]
# print([content["title"],content["author"],content["time"],content["info"],content["zh"],content["en"]])

