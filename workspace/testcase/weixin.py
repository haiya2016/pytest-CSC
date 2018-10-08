# -*- coding: utf-8 -*-

import time
import json
import requests
import re
import random
import math
from selenium import webdriver


# 微信公众号账号
user = "phenix1991@live.cn"
# 公众号密码
password = "250214445wjx"
# 设置要爬取的公众号列表
gzlist = ['差评']
# 微信公众号地址
wechat_url = 'https://mp.weixin.qq.com/'

# 登录微信公众号，获取登录之后的cookies信息，并保存到本地文本中
def wechat_login():
    """
    登录微信公众号，获取登录之后的cookies信息，并保存到本地文本中
    """
    global wechat_url
    print("启动浏览器，打开微信公众号登录界面")
    driver = webdriver.Chrome()
    # 打开微信公众号登录页面
    driver.get(wechat_url)
    # 等待5秒钟
    time.sleep(5)
    print("正在输入微信公众号登录账号和密码......")
    # 清空账号框中的内容
    driver.find_element_by_name("account").clear()
    # 自动填入登录用户名
    driver.find_element_by_name("account").send_keys(user)
    # 清空密码框中的内容
    driver.find_element_by_name("password").clear()
    # 自动填入登录密码
    driver.find_element_by_name("password").send_keys(password)
    # 在自动输完密码之后点一下记住我
    driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[3]/label/i').click()
    # 自动点击登录按钮进行登录
    driver.find_element_by_class_name("btn_login").click()
    # 拿手机扫二维码！
    print("请拿手机扫码二维码登录公众号")
    time.sleep(20)
    print("登录成功")
    driver.get(wechat_url)  # 重新载入公众号登录页，登录之后会显示公众号后台首页，从这个返回内容中获取cookies信息
    # 获取cookies
    cookie_items = driver.get_cookies()
    post = {}   # 定义一个空的字典，存放cookies内容
    # 获取到的cookies是列表形式，将cookies转成json形式并存入本地名为cookie的文本中
    for cookie_item in cookie_items:
        post[cookie_item['name']] = cookie_item['value']
    cookie_str = json.dumps(post)
    with open('cookie.txt', 'w+', encoding='utf-8') as f:
        f.write(cookie_str)
    print("cookies信息已保存到本地")

# 爬取微信公众号文章，并存在本地文本中
def get_content(query):
    # query为要爬取的公众号名称
    global wechat_url
    # 设置headers
    header = {
        "HOST": "mp.weixin.qq.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"
        }

    # 读取上一步获取到的cookies 
    with open('cookie.txt', 'r', encoding='utf-8') as f:
        cookie = f.read()
    cookies = json.loads(cookie)

    # 登录之后的微信公众号首页url变化为：https://mp.weixin.qq.com/cgi-bin/home?t=home/index&lang=zh_CN&token=1849751598
    response = requests.get(url=wechat_url, cookies=cookies)
    # 获取token信息你
    token = re.findall(r'token=(\d+)', str(response.url))[0]

    # 搜索微信公众号的接口地址
    search_url = f'{wechat_url}cgi-bin/searchbiz?'
    # 搜索微信公众号接口需要传入的参数，有三个变量：微信公众号token、随机数random、搜索的微信公众号名字
    query_id = {
        'action': 'search_biz',
        'token' : token,
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1',
        'random': random.random(),
        'query': query,
        'begin': '0',
        'count': '5'
        }  
    # 打开搜索微信公众号接口地址，需要传入相关参数信息如：cookies、params、headers
    search_response = requests.get(search_url, cookies=cookies, headers=header, params=query_id)
    # 取搜索结果中的第一个公众号
    lists = search_response.json().get('list')[0]
    # 获取这个公众号的fakeid，后面爬取公众号文章需要此字段
    fakeid = lists.get('fakeid')

    # 微信公众号文章接口地址
    appmsg_url = f'{wechat_url}cgi-bin/appmsg?'
    # 搜索文章需要传入几个参数：登录的公众号token、要爬取文章的公众号fakeid、随机数random
    query_id_data = {
        'token': token,
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1',
        'random': random.random(),
        'action': 'list_ex',
        'begin': '0',# 不同页，此参数变化，变化规则为每页加5
        'count': '5',
        'query': '',
        'fakeid': fakeid,
        'type': '9'
        }
    # 打开搜索的微信公众号文章列表页
    appmsg_response = requests.get(appmsg_url, cookies=cookies, headers=header, params=query_id_data)
    # 获取文章总数
    max_num = appmsg_response.json().get('app_msg_cnt')
    # 每页至少有5条，获取文章总的页数，爬取时需要分页爬
    num = math.ceil(int(max_num) / 5)
    # 起始页begin参数，往后每页加5
    begin = 0
    # 设置代理ip
    proxy = {
            'http':'http://117.85.105.170:808',
            'http':'http://61.145.194.26:8080',
            'http':'http://112.74.160.144:80',
            'http':'http://183.129.244.17:21231',
            'http':'http://183.129.244.17:10800',
            'http':'http://113.200.81.90:34854',
            'http':'http://1.48.72.146:8118',
            'http':'http://183.129.244.13:18186',
            'https':'https://117.85.105.170:808'
            }
    while num + 1 > 0:
        query_id_data = {
            'token': token,
            'lang': 'zh_CN',
            'f': 'json',
            'ajax': '1',
            'random': random.random(),
            'action': 'list_ex',
            'begin': f'{begin}',
            'count': '5',
            'query': '',
            'fakeid': fakeid,
            'type': '9'
            }
        print('正在翻页：--------------', begin)

        # 获取每一页文章的标题和链接地址，并写入本地文本中
        query_fakeid_response = requests.get(appmsg_url, cookies=cookies, headers=header, params=query_id_data)

        fakeid_list = query_fakeid_response.json().get('app_msg_list')
        for item in fakeid_list:
            content_link = item.get('link')
            content_title = item.get('title')
            print(content_title)
            fileName = query+'.txt'
            with open(fileName, 'a', encoding='utf-8') as fh:
                fh.write(content_title + ":\n" + content_link + "\n")
        num -= 1
        begin = begin + 5
        time.sleep(random.uniform(1,3))  # 随机休眠1到3秒

if __name__ == '__main__':
    # try:
    wechat_login()
    #登录之后，通过微信公众号后台提供的微信公众号文章接口爬取文章
    for query in gzlist:
        #爬取微信公众号文章，并存在本地文本中
        print("开始爬取公众号：" + query)
        get_content(query)
        print("爬取完成")
    # except Exception as e:
    #     print(str(e))