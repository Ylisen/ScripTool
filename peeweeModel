#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021-1-7 15:21
# @Author : admin
# @File : model
# @Software: PyCharm
# @Contact : xxx.com
# @Desc :

import datetime
from peewee import BooleanField, CharField, DateField, DateTimeField, IntegerField, Model, MySQLDatabase, TextField


database = MySQLDatabase('my_test_db', user='test', password='123456',
                         host='10.19.200.89', port=9999)


class BaseModel(Model):
    create_time = DateTimeField(default=datetime.datetime.now)
    update_time = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database


# 定义Person
class Person(BaseModel):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = database


# 创建表
# Person.create_table()

# 创建表也可以这样, 可以创建多个
database.create_tables([Person])

if __name__ == '__main__':
    # 增
    p = Person(name='ligalfogn', birthday=datetime.date(1999, 12, 20), is_relative=True)
    p.save()

    # 删除姓名为perter的数据
    # Person.delete().where(Person.name == 'perter').execute()  # 返回成功处理的行数

    # # 已经实例化的数据, 使用delete_instance
    # p = Person(name='liuchungui', birthday=datetime.date(1999, 12, 20), is_relative=False)
    # p.id = 2
    # p.save()
    # p.delete_instance()

    # # 已经实例化的数据,指定了id这个primary key,则此时保存就是更新数据
    # p = Person(name='liuchungui', birthday=datetime.date(1990, 12, 20), is_relative=False)
    # p.id = 1
    # p.save()
    
    # # 更新birthday数据
    # q = Person.update({Person.birthday: datetime.date(1983, 12, 21)}).where(Person.name == 'liuchungui')
    # q.execute()
    
    # # 查询单条数据
    # p = Person.get(Person.name == 'liuchungui')
    # print(p.name, p.birthday, p.is_relative)
    
    # # 使用where().get()查询
    # p = Person.select().where(Person.name == 'liuchungui').get()
    # print(p.name, p.birthday, p.is_relative)
    #
    # # 查询多条数据
    # persons = Person.select().where(Person.is_relative == True)
    # for p in persons:
    #     print(p.name, p.birthday, p.is_relative)
