#!/usr/bin/python

from Tools.datetimetool import DateTimeTool
import logging
from DbAccess import DBHelper

SOCKET_TIMEOUT = 1

class DbAccesser:
    def __init__(self,host,user,pwd,db):
        self._dbHelper = DBHelper(host,user,pwd,db)
        self._logger = logging.getLogger("root")


    def RecordMonitor(self,domain,url,ip,status,isVip):
        sqlStr = 'insert into MonitorRecord(domain,WebIP,MonStatus,monTime,isVip,monUrl) VALUES (%s,%s,%s,%s,%s,%s)'
        params = (domain,ip,status,DateTimeTool.GetCurrentTimeStr(),isVip,url)
        try:
            self._dbHelper.ExcuteNoneQuery(sqlStr,params)
        except Exception as e:
            logging.error("记录监控信息错误",e.args[1])

    def GetDayStat(self,domain,url,ip,isVip):
        sqlStr = "select count(1) from DayStat where Domain=%s and ip=%s and isVip=%s and monUrl=%s"
        params = (domain,ip,isVip,url)
        try:
            self._dbHelper.ExcuteScalarQuery(sqlStr,params)
        except Exception as e:
            self._logger.error('获取按日统计错误：',e.args[1])

