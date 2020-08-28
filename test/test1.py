# import mysql.connector
#
# conn=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='admin',
#     database = 'test')
# print(conn)
#
# mycursor = conn.cursor()  # 光标行
# mycursor.execute("show databases")	# 展示数据库
# for x in mycursor:
#     print(x)

# mycursor.execute('select * from emp')
# res = mycursor.fetchall()
# print(res)

# mycursor.execute('select * from emp')
# res = mycursor.fetchone()
# print(res)

# mycursor.execute('select * from emp')
# res = mycursor.fetchmany(3)
# print(res)

# import mysql.connector
#
# conn=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='admin',
#     database = 'test')
# print(conn)
#
# mycursor = conn.cursor()  # 光标行
# ssql='insert into emp(id,name) values(%s,%s)'
# sval=(9,'susu')
# mycursor.execute(ssql,sval)
# print(mycursor.rowcount)
# conn.commit()   # 数据表内容有更新，必须使用到该语句
# print(mycursor.rowcount,'记录插入成功！')
# mycursor.execute('select * from emp where id=9')
# res=mycursor.fetchall()
# print(res)


# import mysql.connector
#
# conn=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='admin',
#     database = 'test')
# print(conn)
#
# mycursor = conn.cursor()  # 光标行
# ssql='insert into emp(id,name,dep_id,salary) values(%s,%s,%s,%s)'
# sval=[(11,'花花',1,22000),(12,'月',3,10500),(13,'liming',1,8000)]
# mycursor.executemany(ssql,sval)
# print(mycursor.rowcount)
# conn.commit()   # 数据表内容有更新，必须使用到该语句
# print(mycursor.rowcount,'记录插入成功！')
# mycursor.execute('select * from emp limit 10,3')
# res=mycursor.fetchall()
# print(res)


# import pymysql
# # 打开数据库连接
# db = pymysql.connect("localhost","root","admin","test" )
# # 使用 cursor() 方法创建一个游标对象
# cursor = db.cursor()
# # 使用 execute() 方法执行 SQL 查询
# cursor.execute("select  * from dep")
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
# print (data)
# # 关闭数据库连接
# db.close()


import pymysql

db = pymysql.connect("localhost", "root", "admin", "test")
cursor = db.cursor()
cursor.execute("drop table if exists testcodeinfo")
# 定义要执行的SQL语句
ssql = """create table testcodeinfo(id int primary key auto_increment,
		sname varchar(20),
		classname varchar(100),
		age int)"""
# 执行SQL语句
cursor.execute(ssql)
db.close()