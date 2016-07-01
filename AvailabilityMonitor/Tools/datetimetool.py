import time

class DateTimeTool:

    @staticmethod
    def GetCurrentTimeStr():
        curTime = time.localtime(time.time())
        return time.strftime('%Y-%m-%d %H:%M:%S', curTime)