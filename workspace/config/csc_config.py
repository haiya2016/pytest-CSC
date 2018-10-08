"""
    csc相关配置
"""
import pymysql

URL = "https://192.168.208.70:8099/csc/index.html"
DB = pymysql.connect(
    host='192.168.219.227',
    port=3306,
    user='csc',
    password='csc',
    db='csc')
