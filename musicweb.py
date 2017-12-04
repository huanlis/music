#/usr/bin/python
# -*- coding:utf-8 -*-
#-------------------------
#文件: musicweb.py
#作者: String
#邮箱: 18093329352@163.com
#时间: 17-11-29 下午8:23
#-------------------------

from tornado import web, httpserver, ioloop
import pymysql

# 路由 主页面
class MainPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        # 主页面
        self.render('templates/index.html')


# 路由 注册页面
class SignHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('templates/sign.html')

    def post(self, *args, **kwargs):
        # 获得页面post信息
        netname = self.get_argument('netname')
        netacc = self.get_argument('netacc')
        passwdone = self.get_argument('passwdone')
        passwdtwo = self.get_argument('passwdtwo')
        sex = self.get_argument('sex')
        phone = self.get_argument('phone')
        # 判断信息是否完整
        if netacc and netname and passwdtwo and passwdone and sex and phone:
            if passwdone and passwdtwo:
                cursor.execute()
            else:
                self.write('两次输入的密码不一样！')
        else:
            print('请将信息填写完整！')

# 路由 登陆界面
class loginHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('templates/login.html')

    def post(self, *args, **kwargs):
        # 获得登陆信息
        netacc = self.get_argument('netacc')
        passwd = self.get_argument('passwd')
        # 进行判断
        if netacc and passwd:
            print(netacc, passwd)
        else:
            self.write('请检查账号或密码是否正确！')

#路由注册
application = web.Application([(r'/index', MainPageHandler),
                               (r'/sign', SignHandler),
                               (r'/login', loginHandler),])


if __name__ == '__main__':
    # 链接数据库
    conn = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           passwd='jiangyan1921',
                           db='music',
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    # 创建游标
    cursor = conn.cursor()
    # 启动服务
    http_server = httpserver.HTTPServer(application)
    # 端口监听
    http_server.listen(8080)
    ioloop.IOLoop.current().start()


