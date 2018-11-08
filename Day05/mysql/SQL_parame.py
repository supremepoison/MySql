import pymysql
db = pymysql.connect(host = 'localhost', user = 'root', password = '123456', database = 'studb5',charset = 'utf8')
cur = db.cursor()
while True:
    c = input('按q退出,按回车继续')
    if c.strip().lower() == 'q':
        break    
    name = input('请输入姓名:')
    score = input('请输入成绩:')
    try:
        ins = 'insert into t1(name,score) values(%s,%s)'
        # ins = 'insert into t1(name,score) values("%s","%s")' % (name,score)

        cur.execute(ins,[name,score])
        # cur.execute(ins)

        db.commit()
        print('ok')
    except Exception as e:
        db.rollback()
        print('Failed',e)
cur.close()
db.close()

