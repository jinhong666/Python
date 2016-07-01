#! /usr/bin/env python
#coding=utf-8
#author: ddl
#desc: app main
#---------------------
#2016-06-22 created
#---------------------

import time, os, sched,AmConfig.appconf,WebAccess.webaccesser
from DbAccess.dbaccesser import DbAccesser
import logging
import logging.config
import logging.handlers

class Worker:
    def __init__(self):
        startPath = os.path.split(os.path.realpath(__file__))[0]
        configPath = os.path.join(startPath, "Conf")
        mainConfig = os.path.join(configPath, "am.conf")
        self._conf = AmConfig.appconf.AppConf(mainConfig)
        self._conf.ReadDomainConfig(configPath)
        self._schedule = sched.scheduler(time.time, time.sleep)
        self._webAccesser = WebAccess.webaccesser.WebAccesser()
        self._webAccesser.SetUserAgent("ycapp web monitor")
        self._db = DbAccesser(self._conf.DbHost,self._conf.DbUserName,self._conf.DbPassword,self._conf.DbName)

    def perform_command(self,cmd, inc):
        # 安排inc秒后再次运行自己，即周期运行
        self._schedule.enter(inc, 0, self.perform_command, (cmd, inc))
        self.work()


    def start(self):
        self._schedule.enter(0, 0, self.perform_command, (None, self._conf.MonitorInterval))
        self._schedule.run()

    def work(self):
        for domainConf in self._conf.DomainConfs:
            logging.info("perform domain " + domainConf.DomainName + "[" + domainConf.VIP + "]")
            self._checkDomain(domainConf)
        print("\n")

    def _checkDomain(self,domainConf):
        self._webAccesser.SetDomainName(domainConf.DomainName)
        self._webAccesser.SetWebIp(domainConf.VIP)
        for urlKey in list(domainConf.UrlDic.keys()):
            url = domainConf.UrlDic[urlKey]
            fullUrl = 'http://' + domainConf.DomainName + url
            resData = self._webAccesser.RequestUrl(url)
            status = 0
            if len(resData) == 0:
                logging.info( "Error\t" + fullUrl)
                status =0
            else:
                logging.info("OK\t" + fullUrl)
                status = 1
            self._db.RecordMonitor(domainConf.DomainName,url, domainConf.VIP, status, True)








def main():
    #logging.basicConfig(level=logging.DEBUG)
    logging.config.fileConfig("Conf/log.conf")
    logging.handlers.TimedRotatingFileHandler
    logging.info("Start!")
    worker = Worker()
    worker.start()

if __name__ == '__main__':
    main()