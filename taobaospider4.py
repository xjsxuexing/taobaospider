#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = ['xjs <jingsheng_xu@bacic5i5j.com>']

import requests
import json
import re
import pandas as pd
import pymysql


class TaobaoGoods(object):
    def __init__(self):
        self.result = []
        self.source = []

    def extract_link(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='xjs123', db='mysql', use_unicode=True,
                               charset="utf8")

        cur = conn.cursor()
        cur.execute("USE taobao")
        sql = 'SELECT link FROM taobao_list_link LIMIT 1'
        cur.execute(sql)
        result = cur.fetchall()
        for result1 in result:
            for result2 in result1:
                self.result.append(result2)
        #print(self.result)


    def parse_link(self):
        for result_l in self.result:
            html = requests.get(result_l)
            #self.source.append(html.content.decode('utf-8'))
            print(html.content.decode('gbk'))



if __name__ == '__main__':
   taobaogoods = TaobaoGoods()
   taobaogoods.extract_link()
   taobaogoods.parse_link()

















