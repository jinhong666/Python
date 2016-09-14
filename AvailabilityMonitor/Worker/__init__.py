#! /usr/bin/env python
#author: ddl
#desc: main worker
#---------------------
#2016-07-25 created
#---------------------
from DbAccess.dbaccesser import DbAccesser
from WebAccess.webaccesser import WebAccesser

class MainWorker:
    def __init__(self,mainConf,logger):
        self._logger = logger
        self._conf = mainConf
        self._db = DbAccesser(self._conf.DbHost, self._conf.DbUserName, self._conf.DbPassword, self._conf.DbName)
        self._webAccesser = WebAccesser('')
        self._webAccesser.SetUserAgent("ycapp web monitor")

    def Work(self):
        for domainConf in self._conf.DomainConfs:
            self._checkDomain(domainConf)

    def _checkDomain(self, domainConf):
        for urlKey in list(domainConf.UrlDic.keys()):
            url = domainConf.UrlDic[urlKey]
            fullUrl = 'http://' + domainConf.DomainName + url
            self._webAccesser.SetUrl(fullUrl)
            self._checkServerByIP(domainConf.DomainName,domainConf.VIP,True)
            for srcIP in domainConf.SrcIpList:
                self._checkServerByIP(domainConf.DomainName,srcIP,False)


    def _checkServerByIP(self, domainName,ip,isVIP):
        self._logger.info("perform domain ip:" + "[" + ip + "]" + domainName)
        self._webAccesser.SetDomainIp(ip)
        status = self._checkServer()
        self._db.RecordMonitor(domainName, self._webAccesser.Url, ip, status, isVIP)


    def _checkServer(self):
        resData = self._webAccesser.Request()
        if len(resData) == 0:
            self._logger.info("Error\t" + self._webAccesser.Url)
            status = 0
        else:
            self._logger.info("OK\t" + self._webAccesser.Url)
            status = 1
        return status


