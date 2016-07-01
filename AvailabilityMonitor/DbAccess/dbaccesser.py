#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql.cursors
from Tools.datetimetool import DateTimeTool
import logging

SOCKET_TIMEOUT = 1

class DbAccesser:
    def __init__(self,host,user,pwd,db):
        self._host = host
        self._user = user
        self._pwd = pwd
        self._db = db

    def _getConnection(self):
        conn = None
        try:
            conn = pymysql.connect(host=self._host,user=self._user,password=self._pwd,db=self._db,charset='utf8mb4',
                                   connect_timeout=2.0,read_timeout=5.0,write_timeout=5.0,
                                     cursorclass=pymysql.cursors.DictCursor)
            conn.connect_timeout = 1.0
        except Exception as e:
            logging.error("数据库连接错误")
            logging.error(e)
        return conn

    def RecordMonitor(self,domain,url,ip,status,isVip):
        conn = self._getConnection()
        if conn is None:
            return
        try:
            with conn.cursor() as cursor:
                sqlStr = 'insert into MonitorRecord(domain,WebIP,MonStatus,monTime,isVip,monUrl) VALUES (%s,%s,%s,%s,%s,%s)'
                cursor.execute(sqlStr,(domain,ip,status,DateTimeTool.GetCurrentTimeStr(),isVip,url))
                conn.commit()
        except Exception as e:
            logging.error("记录监控信息错误",e.args[1])
        finally:
            if conn.open:
               conn.close()

