from mysqlpython import MysqlPython
from hashlib import sha1

#接受用户输入的用户名和密码
uname = input('请输入用户名:')
pwd = input('请输入密码:')


#把用户输入的密码用sha1加密
s1 = sha1()#创建一个sha1加密对象
s1.update(pwd.encode('utf8'))
pwd2 = s1.hexdigest()   #返回16进制加密结果



#两个密码做对比
test = MysqlPython('studb5')
sel = 'select password from user where username = %s'
r = test.all(sel,[uname])
# print(r)

if len(r) == 0:
    print('用户名不存在')
elif pwd2 ==r[0][0]:
    print('登录成功')
else:
    print('密码错误')