# -*- coding: utf-8 -*-


import pymysql  #导入 pymysql
     
'''

https://blog.csdn.net/qq_37176126/article/details/72824106

create database test;
use test;
create table user(id int not null,username varchar(500) not null,
password varchar(500) not null);

insert into user values(1,"zhang","1111");
insert into user values(2,"lisi","1234");
insert into user values(4,"liu","4545");

'''

#打开数据库连接
conn= pymysql.connect(host="localhost",
                user="root",
                password="123456",
                db="test",
                port=3306)
             
# 使用cursor()方法获取操作游标
cur = conn.cursor()
             
#1.查询操作
# 编写sql 查询语句  user 对应我的表名
sql = "select * from user"
try:
    cur.execute(sql)    #执行sql语句
             
    results = cur.fetchall()    #获取查询的所有记录
    print("id","name","password")
    #遍历结果
    for row in results :
        id = row[0]
        name = row[1]
        password = row[2]
        print(id,name,password)
except Exception as e:
    raise e
finally:
    conn.close()  #关闭连接