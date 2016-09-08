#!/usr/bin/python

import pymysql.cursors

class DBHelper:
    def __init__(self,host,user,pwd,db):
        self._host = host
        self._user = user
        self._pwd = pwd
        self._db = db

    def _getConnection(self):
        conn  = pymysql.connect(host=self._host, user=self._user, password=self._pwd, db=self._db, charset='utf8mb4',
                                   connect_timeout=1.0, read_timeout=2.0, write_timeout=3.0,
                                   cursorclass=pymysql.cursors.DictCursor)
        return conn

    def ExcuteNoneQuery(self,sqlStr,params):
        conn = self._getConnection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sqlStr, params)
                conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            if conn.open:
                conn.close()

    def ExcuteScalarQuery(self,sqlStr,params):
        conn = self._getConnection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sqlStr, params)
                resuSet = cursor.fetchall()
        finally:
            if conn.open:
                conn.close()

        if resuSet is None or len(resuSet) == 0:
            return 0
        resu = resuSet[0][0]
        return resu
