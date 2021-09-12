# 启动虚环境
source ./bin/activate

# 启动内置web服务器
python manage.py runserver 0.0.0.0:8001

# 生成数据迁移文件
python manage.py makemigrations app

# 移植到数据库
python manage.py migrate

# superuser
admin/1a598560b1

# suit
pip install django-suit

#Django REST Framework