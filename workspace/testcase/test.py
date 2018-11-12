#!/usr/bin/python
# -*- coding: UTF-8 -*-

#发布会查询接口测试代码
import unittest
import requests

class GetEventListTest(unittest.TestCase):

    def test_req_get(self,url,params,headers):
        try:
            r = requests.get(url,params=params,headers=headers)
            #转换为python类型的字典格式,json包的响应结果，调用json(),转换成python类型
            json_r = r.json()
            return json_r
        except BaseException as e:
            print("请求不能完成:",str(e))

u'''下面为测试代码'''
url = "http://v.juhe.cn/laohuangli/d"
params = {"key":"e711bc6362b3179f5a28de7fd3ee4ace","date":"2016-5-14"}
headers = {}
req = GetEventListTest()
ss = req.test_req_get(url,params,headers)
print(ss)

a = '{{:{}}}{{:{}}}'.format(25,10)
print(a)