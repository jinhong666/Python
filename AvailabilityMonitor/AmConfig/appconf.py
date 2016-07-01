#!/usr/bin/python
# -*- coding:utf-8 -*-
#author: ddl
#desc: read and store config
#---------------------
#2016-06-17 created
#---------------------

import  configparser,os
import  AmConfig.domainconfig

class AppConf:
    
    @property
    def MonitorInterval(self):
        return self._monitorInterval

    @property
    def DomainConfs(self):
        return self._domainConfs
    
    @MonitorInterval.setter
    def MonitorInterval(self,value):
        if not isinstance(value,int):
            raise ValueError("MonitorInterval must be an integer,unit:second!")
        if value <= 5:
            self._monitorInterval = 5
        self._monitorInterval = value

    @property
    def DbHost(self):
        return self._dbhost

    @DbHost.setter
    def DbHost(self,value):
        if value is None or len(value) == 0:
            raise ValueError("DbHost must not be zero length")
        self._dbhost = value

    @property
    def DbUserName(self):
        return self._dbuser

    @DbUserName.setter
    def DbUserName(self,value):
        if value is None or len(value) == 0:
            raise ValueError("DbUserName must not be zero length")
        self._dbuser = value

    @property
    def DbPassword(self):
        return self._dbpassword

    @DbPassword.setter
    def DbPassword(self,value):
        if value is None or len(value) == 0:
            raise ValueError("DbPassword must not be zero length")
        self._dbpassword = value

    @property
    def DbName(self):
        return self._dbname

    @DbName.setter
    def DbName(self,value):
        if value is None or len(value) == 0:
            raise ValueError("DbName must not be zero length")

    def __init__(self,path):
        self._domainConfs = []
        self._parser = configparser.ConfigParser()
        self._parser.read(path)
        self._monitorInterval = self._parser.getint("appconfig", "monitorinterval")
        self._dbhost = self._parser.get("db","host")
        self._dbuser = self._parser.get("db","user")
        self._dbpassword = self._parser.get("db","pwd")
        self._dbname = self._parser.get("db","dbname")


    def ReadDomainConfig(self,path):
        domainCfgPath = os.path.join(path,"DomainConf")
        for confFile in AppConf.GetDomainConfigFiles(domainCfgPath):
            domainConf = AmConfig.domainconfig.DomainConf(confFile)
            self._domainConfs.append(domainConf)

    @staticmethod
    def GetDomainConfigFiles(path):
        domainConfigFiles = []
        for confFile in os.listdir(path):
            fullPath = os.path.join(path,confFile)
            if os.path.isfile(fullPath):
                domainConfigFiles.append(fullPath)
        return domainConfigFiles





