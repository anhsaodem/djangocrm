# Starting project
1.Tạo thư mục Django CRM dcrm
2.Tạo virtenv
```ComandLine
python -m venv virtenv
```
3. Activate venv
```ComandLine
source virtenv/Scripts/activate
```
4. Cài đặt database
```ComandLine
pip install mysql
```
5. Cài mysql-connector
```ComandLine
pip insatll mysql-connector-python
```
6. Cài đặt django
```ComandLine
pip install django
```
7. Tạo project django
```ComandLine
django-admin startproject dcrm
```
8. Tạo app tại thư mục dcrm có chứa manage.py và thêm app vào settings
```ComandLine
python manage.py startapp website
```

9. Kết nối database vào file settings.py 
```ComandLine
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dcrmproject',
        'USER': 'root',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT':'3306'
    }
}
```
10. Tạo file quản lý database tại thư mục ngang manage.py
```ComandLine
touch mydb.py
```
11. Tạo và kết nối db khi chạy file mydb.py
```ComandLine
import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '12345'
)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE dcrmproject")
print('ALL DONE')
```
```ComandLine
python mydb.py
```
12. Migrate migrations có sẵn của django
```ComandLine
python manage.py migrate
```
