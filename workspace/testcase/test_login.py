# coding=utf-8
'''
Created on 2018-9-9
@author: wjx
Project: 登录模块的测试用例
'''

import pytest
from selenium import webdriver
from workspace.pages.login_page import LoginPage


class TestLoginCSC():
    """
          登录CSC的测试用例
    """

    def setup_method(self):
        """
            初始化，在每个方法前运行
        """
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.set_window_size(1366, 768)
        self.url = "https://192.168.208.70:8099/csc/index.html"
        # pass

    @pytest.mark.parametrize('casename, username, password, asserts',
                             [("user_null", '', 'password', '账号不能为空！'),
                              ("pwd_null", 'admin', '', '密码不能为空！'),
                              ("local_login", 'admin', '1234567890', 'admin'),
                              ("ad_login", 'wjx', 'Admin123', 'wjx')])
    def test_login_csc(self, casename, username, password, asserts):
        '''
            测试使用不同的账号密码组合进行登陆测试
        '''
        login_page = LoginPage(self.driver, self.url)   # 创建一个登陆页面的实例
        login_page.open()
        login_page.input_username(username)
        login_page.input_password(password)

        if casename == 'ad_login':             # 是否切换Ad域登录
            login_page.switch_usertype()
        login_page.click_submit()

        if login_page.on_page('WinCloud-CSC'):  # 判断登陆情况和tip信息
            assert login_page.show_userid(asserts)
        else:
            assert login_page.show_msg() == asserts

    def teardown_method(self):
        """
            在每个测试用例结束后运行，关闭浏览器
        """
        self.driver.quit()
        # pass


if __name__ == '__main__':
    pytest.main(['-q', './workspace/testcase/test_login.py'])
    