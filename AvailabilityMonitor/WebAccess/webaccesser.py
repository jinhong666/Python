#!/usr/bin/python
# -*- coding:utf-8 -*-
#author: ddl
#desc: request url get data
#---------------------
#2016-06-20 created
#---------------------

import http.client

class WebAccesser:
    def __init__(self):
        self._agent = ""
        self._domainName = ""
        self._ip = ""
        self._protocol = "http"

    def SetUserAgent(self,agent):
        self._agent = agent

    def SetDomainName(self,domainName):
        self._domainName = domainName

    def SetWebIp(self,ip):
        self._ip = ip

    def SetProtocol(self,protocol):
        self._protocol = protocol

    def RequestUrl(self,url):
        headers = {
            'User-Agent' : self._agent,
            'Host' : self._domainName
        }
        if self._protocol == 'https':
            conn = http.client.HTTPConnection(self._ip)
        else:
            conn = http.client.HTTPSConnection(self._ip)
        conn.timeout = 2.0
        conn.request("GET",url,'',headers)
        res = conn.getresponse()
        resData = ''
        if res.status == 200:
            resData = res.read()
        return resData
