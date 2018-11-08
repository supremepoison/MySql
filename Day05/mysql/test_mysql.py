from mysqlpython import MysqlPython

sqlh = MysqlPython('studb5')
dele = 'delete from t1 where name = " "'
sqlh.add_del_update(dele)
