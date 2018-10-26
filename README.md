# django_crud


django_crud是一个简单的增删改查练习。



Django

1.Django是一个基于python的高级web开发框架。

2.Django安装
 http://www.runoob.com/django/django-install.html
3.mac 上面安装pip
https://blog.csdn.net/mike__lee/article/details/72593684
4.创建Django项目
django-admin start project myblog
5.启动项目
进入根目录中
python3 manage.py runserver
python3 manage.py runserver  9999—以特殊端口启动
6.项目结构介绍
manage.py ——项目管理器
7.wsgi.py
python应用与web服务器之间的接口
8.urls.py
url配置文件
9.settings.py
整个项目的核心配置文件
10._init_.py



11.创建Django应用
python3 manage.py  startapp blog


12.models映射生成数据库表
python3 manage.py makemigrations
 python3 manage.py migrate

13.创建超级用户密码
python3 manage.py  createsuperuser
localhost:8000/admin
