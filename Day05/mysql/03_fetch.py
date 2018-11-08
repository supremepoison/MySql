import pymysql
db = pymysql.connect(host = 'localhost', user = 'root', password = '123456', database = 'studb5',charset = 'utf8')
cur = db.cursor()
try:
    sel = 'select * from t1'
    #得到一堆查询结果,放到了cur游标对象中
    cur.execute(sel)
    
    #取走游标对象里的一条记录
    data1 = cur.fetchone()
    print(data1)
    print()

    #取走游标对象里的二条记录
    data2 = cur.fetchmany(2)
    # print(data2)
    for i in data2:
        print(i)
    print()

    #取走游标对象里的剩下的记录
    data3 = cur.fetchall()
    print(data3)
    
except Exception as e:
    
    print('failed',e)
cur.close()
db.close()