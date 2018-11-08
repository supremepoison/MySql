#在db5库中t2表插入一条记录(4,'王维',80)

import pymysql

#1.创建数据库连接对象
db = pymysql.connect(host = 'localhost', 
                    user = 'root', 
                    password = '123456', 
                    database = 'studb5', 
                    charset = 'utf8')
#2.创建游标对象(利用数据库的对象)
cursor = db.cursor()

#3.执行sql命令(利用游标对象)
cursor.execute('insert into t1 values(4,"王维",80);')



#4.提交到数据库执行(commit())
db.commit()
print('ok')

#5.关闭游标对象
cursor.close()
#6.关闭数据库连接对象
db.close()