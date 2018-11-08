'''
在t1表中增加1条记录
在t1表中把李白成绩改为100分
在t1表中删除一条记录
'''

import pymysql
try:
    db = pymysql.connect(host = 'localhost', user = 'root', password = '123456', database = 'studb5',charset = 'utf8')
    cur = db.cursor()
    cur.execute('insert into t1 values(5,"辛弃疾",21);')
    cur.execute('update t1 set score = 100 where name = "李白";')
    cur.execute('delete from t1 where name = "王维";')
    print('ok')
    db.commit()
except Exception as e:
    db.rollback()
    print('Failed',e)

cur.close()
db.close()