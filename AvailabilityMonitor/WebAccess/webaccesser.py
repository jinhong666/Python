#!/usr/bin/python
# -*- coding:utf-8 -*-
#author: ddl
#desc: request url get data
#---------------------
#2016-06-20 created
#---------------------

import http.client,re

class WebAccesser:
    @property
    def Protocol(self):
        return self._protocol

    @property
    def DonmainName(self):
        return self._domainName
    @property
    def Port(self):
        return self._port

    @property
    def Path(self):
        return self._path;

    @property
    def QueryString(self):
        return self._querystr

    @property
    def Url(self):
        return self._fullUrl

    def __init__(self,url):
        self._agent = ""
        self._domainName = ""
        self._ip = ""
        self._port = 80
        self._protocol = "http"
        self._path = ''
        self._querystr = ''
        self._fullUrl = ''
        if len(url) > 0:
            self.InitByUrl(url)


    def InitByUrl(self,url):
        pattern = '^(?:([A-Za-z]+):)?(?:\/{0,3})([0-9.\-A-Za-z]+)(?::(\d+))?(\/[^?#]*)?(?:\?([^#]*))?(?:#(.*))?$'
        m=re.search(pattern,url)
        if m.group(0) != url:
            raise ValueError('given url is not valid')
        self._fullUrl = url
        self._protocol = m.group(1)
        self._domainName = m.group(2)
        port = m.group(3)
        if port is None or len(port) == 0:
            self._port = 80
        else:
            self._port = int(m.group(3))
        self._path = m.group(4)
        self._querystr = m.group(5)

        #for i in range(m.lastindex + 1):
        #    print(m.group(i))


    def SetUserAgent(self,agent):
        self._agent = agent

    def SetDomainIp(self,ip):
        self._ip = ip

    def SetUrl(self,url):
        self.InitByUrl(url)
        self._ip = ''



    def Request(self):
        headers = {
            'User-Agent' : self._agent
        }
        host = self._domainName
        if len(self._ip) > 0:
            host = self._ip
            headers['Host'] = self._domainName

        if self._protocol == 'https':
            conn = http.client.HTTPSConnection(host)
        else:
            conn = http.client.HTTPConnection(host)
        conn.timeout = 2.0
        absUrl = self._path
        if self._querystr is not None and len(self._querystr) > 0:
            absUrl += '?' + self._querystr
        conn.request("GET",absUrl ,'',headers)
        res = conn.getresponse()
        resData = ''
        if res.status == 200:
            resData = res.read()
        return resData
