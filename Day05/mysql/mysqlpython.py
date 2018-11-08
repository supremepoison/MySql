from pymysql import *

class MysqlPython:
    def __init__(self,database,host = 'localhost', user = 'root', password = '123456', charset ='utf8', port = 3306):
        self.databsae = database
        self.host = host
        self.user= user
        self.password = password
        self.charset = charset
        self.port = port

    #创建数据库连接和游标对象
    def open(self):
        self.db = connect(host = self.host, 
                            user= self.user, 
                            password = self.password, 
                            database= self.databsae, 
                            charset = self.charset, 
                            port = self.port)

        self.cur = self.db.cursor()

    #关闭游标对象和数据库连接对象    
    def close(self):
        self.cur.close()
        self.db.close()

    #执行sql命令
    def add_del_update(self,sql,L = []):
        self.open()

        self.cur.execute(sql, L)
        self.db.commit()

        self.close()
        pass
    def all(self,sql,L = []):
        self.open()
        self.cur.execute(sql,L)
        result = self.cur.fetchall()
        return result
        self.close()
        
        
    
if __name__ == '__main__':
    sqlh = MysqlPython('studb5')
    update = 'update t1 set score = 100 where name = "辛弃疾"'
    sqlh.a_d_u(update)

    r= sqlh.all('select * from t1')
    for i in r:
        print(i)