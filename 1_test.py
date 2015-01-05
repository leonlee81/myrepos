#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import string
import MySQLdb
from collections import namedtuple

user = ''
pwd = ''
host = ''
db = 'dbpara01'
port = 3306

try:
    cnx = MySQLdb.connect(host=host,db=db,user=user,passwd=pwd,port=int(port),connect_timeout=2,charset='utf8')
    cur = cnx.cursor()
    cur.execute("select id,gateway_id,order_code,end_user_id from olp_pay_log order by id limit 10")
    OlpPay = namedtuple('OlpPay', 'id, gateway_id, order_code, end_user_id')
    for olp in map(OlpPay._make, cur.fetchall()):
        print   "%d,%s" %(olp.id, olp.order_code)
        print   (int(olp.id), str(olp.order_code))
        print    int(olp.id), str(olp.order_code)

except MySQLdb.Error,e:
    pass
    print "Mysql Error %d: %s" %(e.args[0],e.args[1])

finally:
    #finish and close connection
    cur.close()
    cnx.close()

