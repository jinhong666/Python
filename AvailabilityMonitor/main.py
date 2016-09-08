#! /usr/bin/env python
#coding=utf-8
#author: ddl
#desc: app main
#---------------------
#2016-06-22 created
#---------------------

import time, os, sched,AmConfig.appconf

import logging
import logging.config
import logging.handlers
from Worker import MainWorker

class MainLoop:
    def __init__(self,logger):
        startPath = os.path.split(os.path.realpath(__file__))[0]
        configPath = os.path.join(startPath, "Conf")
        mainConfig = os.path.join(configPath, "am.conf")
        self._logger = logger
        self._conf = AmConfig.appconf.AppConf(mainConfig)
        self._conf.ReadDomainConfig(configPath)
        self._schedule = sched.scheduler(time.time, time.sleep)
        self._worker = MainWorker(self._conf,self._logger)



    def perform_command(self,cmd, inc):
        # 安排inc秒后再次运行自己，即周期运行
        self._schedule.enter(inc, 0, self.perform_command, (cmd, inc))
        self._worker.Work()


    def start(self):
        self._schedule.enter(0, 0, self.perform_command, (None, self._conf.MonitorInterval))
        self._schedule.run()


def main():
    #logging.basicConfig(level=logging.DEBUG)
    logging.config.fileConfig("Conf/log.conf")
    #logging.handlers.TimedRotatingFileHandler
    logger = logging.getLogger("root")
    logger.info("Start!")
    mainLoop = MainLoop(logger)
    mainLoop.start()

if __name__ == '__main__':
    main()