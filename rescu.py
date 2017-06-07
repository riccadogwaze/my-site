Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import sqlite3
>>> db = sqlite3.connect('database.db')
>>> db.execute('create table rescu(Name text, Phone number int, email add text, message text')

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    db.execute('create table rescu(Name text, Phone number int, email add text, message text')
OperationalError: near "add": syntax error
>>> db.execute('create table rescu(Name text, Phone number int, email address text, message text')

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    db.execute('create table rescu(Name text, Phone number int, email address text, message text')
OperationalError: near "text": syntax error
>>> db.execute('create table rescu(Name text, Phone number int, email address text, message text)')
<sqlite3.Cursor object at 0x02C0EF60>
>>> 
