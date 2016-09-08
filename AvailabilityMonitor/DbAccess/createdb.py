#!/usr/local/bin/python3

import pymysql.cursors


def getConnection():
    conn = pymysql.connect(host='localhost', user='root', password='rootpwd', db='AvailabilityMonitor', charset='utf8mb4',
                               connect_timeout=2.0, read_timeout=5.0, write_timeout=5.0,
                               cursorclass=pymysql.cursors.DictCursor)
    return conn

def createtableDaystat():
    sql = 'create table Daystat(Id int not NULL auto_increment, \
                                  Domain varchar(50) not NULL, \
                                  WebIp varchar(15) not NULL, \
                                  monDay DATE not NULL, \
                                  FailNum int not NULL ,\
                                  monUrl varchar(254) not NULL ,\
                                  isVip int not NULL ,\
                                  PRIMARY key(Id))'
    excureSql(sql)

def excureSql(sqlStr):
    conn = getConnection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sqlStr)
    except Exception as e:
        print("Ö´ÐÐSQL´íÎó£º", e.args[1])
    finally:
        if conn.open:
            conn.close()

def createstroreprocedure():
    sql = 'create procedure countDayFail (in doname varchar(50),\
     36                                             in ip varchar(15),\
     37                                             in mDay date,\
     38                                             in isV int, \
     39                                             in url varchar(254)) \
     40           BEGIN \
     41             declare failCount int default 0 ;\
     42             SELECT COUNT(1) as failNum into failCount FROM MonitorRecord WHERE DOMAIN =doname and WebIp=ip and monTime between mDay and date_add(mDay,interval 1 day) and monUrl=url and m    onStatus=0; \
     43             INSERT Daystat (Domain,WebIp,monDay,FailNum,monUrl,isVip) VALUES (doname,ip,mDay,failCount,url,isV);\
     44           END '

    excureSql(sql)

createstroreprocedure()
