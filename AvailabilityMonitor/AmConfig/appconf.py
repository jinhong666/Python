#!/usr/bin/python
# -*- coding:utf-8 -*-
#author: ddl
#desc: read and store config
#---------------------
#2016-06-17 created
#---------------------

import  configparser

class AppConf:
    
    @property
    def MonitorInterval(self):
        return self._monitorInterval
    
    @MonitorInterval.setter
    def MonitorInterval(self,value):
        if not isinstance(value,int):
            raise ValueError("MonitorInterval must be an integer,unit:second!")
        if value <= 5:
            self._monitorInterval = 5
        self._monitorInterval = value
        
    
    def __init__(self,path):
        self._parser = configparser.ConfigParser()
        self._parser.read(path)
        self._monitorInterval = self._parser.getint("appconfig", "monitorinterval")




