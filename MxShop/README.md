### 基础环境安装
#### 安装依赖
```python
pip install djangorestframework
pip install django
pip install markdown
pip install django-filter
pip install pillow
pip install pymysql
```
#### 安装xadmin
```python
pip install git+git://github.com/sshwsfc/xadmin.git@django2
pip install git+https://github.com/sshwsfc/xadmin.git@django2
```
#### 安装富文本编辑器
```python
wget -c https://github.com/twz915/DjangoUeditor3/
下载完后将DjangoUeditor拷贝到extra_appa中
```
#### 创建数据库
```python
# 创建数据库
create dataabse mxshop default character set utf8 collate utf8_general_ci;
# 初始化数据表
python manage.py makemigrations
# 同步表
python manage.py migrate
```

