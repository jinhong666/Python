#!/usr/bin/python
# -*- coding:utf-8 -*-
#author: ddl
#desc: read and store config
#---------------------
#2016-06-17 created
#---------------------

import  configparser

class DomainConf:
    @property
    def DomainName(self):
        return self._domainname

    @property
    def VIP(self):
        return self._vip

    @property
    def SrcIpList(self):
        return self._srcIpList

    @property
    def UrlDic(self):
        return self._urlDic

    @property
    def UrlValidDic(self):
        return self._urlValidDic

    def __init__(self,path):
        self._parser = configparser.ConfigParser()
        self._parser.read(path)
        self._domainname = self._parser.get("domain", "domainname")
        self._vip = self._parser.get("domain","vip")
        self._srcIpList = self._parser.get("domain","srcip").split(',')
        self._urlDic = self._readUrlDic()
        self._urlValidDic = self._readValidDic()

    def _readUrlDic(self):
        options = self._parser.options("address")
        urlDic = {}
        for optionName in options:
            urlDic[optionName] = self._parser.get("address",optionName)

        return  urlDic

    def _readValidDic(self):
        options = self._parser.options("valid")
        validDic = {}
        for optionName in options:
            validDic[optionName] = self._parser.get("valid",optionName)

        return  validDic





