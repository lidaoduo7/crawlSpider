# -*- coding: utf-8 -*-


import pymysql
#2.插入操作
conn= pymysql.connect(host="localhost",
                user="root",
                password="123456",
                db="test",
                port=3306)

# 使用cursor()方法获取操作游标
cur = conn.cursor()

sql_insert ="""insert into user(id,username,password) values(5,'wang','1234')"""

try:
	cur.execute(sql_insert)
	#提交
	conn.commit()
except Exception as e:
	#错误回滚
	conn.rollback() 
finally:
	conn.close()