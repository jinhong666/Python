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
        self._webAccesser = WebAccesser()
        self._webAccesser.SetUserAgent("ycapp web monitor")

    def Work(self):
        for domainConf in self._conf.DomainConfs:
            self._checkDomain(domainConf)

    def _checkDomain(self, domainConf):
        self._webAccesser.SetDomainName(domainConf.DomainName)
        self._logger.info("perform domain VIP:" + "[" + domainConf.VIP + "]" + domainConf.DomainName)
        self._checkServerByIp(domainConf, domainConf.VIP, True)
        for srcIP in domainConf.SrcIpList:
            self._logger.info("perform domain SIP:" + "[" + srcIP + "]" + domainConf.DomainName)
            self._checkServerByIp(domainConf, srcIP, False)

    def _checkServerByIp(self, domainConf, ip, isVip):
        self._webAccesser.SetWebIp(ip)
        for urlKey in list(domainConf.UrlDic.keys()):
            url = domainConf.UrlDic[urlKey]
            fullUrl = 'http://' + domainConf.DomainName + url
            resData = self._webAccesser.RequestUrl(url)
            if len(resData) == 0:
                self._logger.info("Error\t" + fullUrl)
                status = 0
            else:
                self._logger.info("OK\t" + fullUrl)
                status = 1
            self._db.RecordMonitor(domainConf.DomainName, url, ip, status, isVip)

