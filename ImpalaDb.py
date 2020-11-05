#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020-11-5 17:45
# @Author : lisen
# @File : ImpalaDb
# @Software: PyCharm
# @Contact : xxx.com
# @Desc :
from impala.dbapi import connect


class ImpalaDb(object):
    def __init__(self, host_port):
        host, port = host_port.split(':')
        self.host = host
        self.port = int(port)
        self.conn = None
        # self.table_fields_map = {}
        self.cur = None

    def close(self):
        """ 关闭连接 """
        if self.conn:
            self.conn.close()

    def get_all_table(self, db_name):
        cur = self.execute('use %s' % db_name)
        isql = 'show tables;'
        cur.execute(isql)
        return [x[0] for x in cur.fetchall()]

    def create_database(self, db_name):
        """
        创建数据库
        """
        isql = "create database IF NOT EXISTS %s" % db_name
        self.execute(isql)

    def execute(self, isql, ):
        if not self.conn:
            self.conn = connect(host=self.host, port=self.port)
        if not self.cur:
            self.cur = self.conn.cursor()
        self.cur.execute(isql)
        return self.cur

    def refresh_table(self, table_name):
        isql = 'REFRESH {table} '.format(table=table_name)
        self.conn.cursor().execute(isql)

    def invalidate_metadata(self, table_name):
        isql = 'invalidate metadata {table} '.format(table=table_name)
        self.execute(isql)

    def compute_incremental_stats(self, table_name):
        isql = 'COMPUTE INCREMENTAL STATS {table} '.format(table=table_name)
        self.execute(isql)


if __name__ == '__main__':
    impala_obj = ImpalaDb('master:21050')
    for tb in impala_obj.get_all_table('test'):
        print(tb)
        
    sql = """ 
    SELECT * FROM test.ods__test limit 10
    """
    cur = impala_obj.execute(sql)
    for item in cur.fetchall():
        print(item)
