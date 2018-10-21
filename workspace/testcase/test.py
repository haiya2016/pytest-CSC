# coding=utf-8
'''
Created on 2018-9-9
@author: wjx
Project: 登录模块的测试用例
'''
import json
import requests
import pytest
from workspace.pages.login_page import LoginPage
from workspace.config.running_config import get_driver


class TestLoginCSC():
    """
        登录CSC的测试用例
    """

    def setup_method(self):
        """
            初始化，在每个方法前运行
        """
        self.driver = get_driver()


    def test_login_csc(self):
        '''
            测试使用不同的账号密码组合进行登陆测试
        '''
        login_page = LoginPage(self.driver)   # 创建一个登陆页面的实例
        login_page.open()
        login_page.input_username('admin')
        login_page.input_password('1234567890')
        login_page.click_submit()
        cookie_items = self.driver.get_cookies()
        print(cookie_items)
        post = {}   # 定义一个空的字典，存放cookies内容
        # 获取到的cookies是列表形式，将cookies转成json形式并存入本地名为cookie的文本中
        for cookie_item in cookie_items:
            post[cookie_item['name']] = cookie_item['value']
        print(post)
        cookie_str = json.dumps(post)
        print(cookie_str)
        cookies = json.loads(cookie_str)
        print(cookies)
        response = requests.get(url='https://192.168.219.227:8099/csc/api/v5.0.0/homepage/user', cookies=cookies, verify=False)
        print(response.text)
        with open('cookie.txt', 'w+', encoding='utf-8') as f:
            f.write(response.text)


    def teardown_method(self):
        """
            在每个测试用例结束后运行，关闭浏览器
        """
        self.driver.quit()
        # pass


if __name__ == '__main__':
    pytest.main(['-q', './workspace/testcase/test.py'])
