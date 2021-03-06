'''
@Description: 
@Author: wjx
@Date: 2018-09-23 17:06:51
@LastEditors: wjx
@LastEditTime: 2018-11-20 16:03:54
'''
# coding=utf-8


import pytest
from workspace.pages.login_page import LoginPage
from workspace.config.running_config import get_driver


class TestLoginCSC():
    """
        登录CSC的测试用例
    """

    @pytest.fixture(scope='function')
    def init(self):
        '''
        获取和退出浏览器
        '''
        self.driver = get_driver()
        yield
        self.driver.quit()


    @pytest.mark.parametrize('casename, username, password, asserts',
                             [("用户名为空", '', 'password', '账号不能为空！'),
                              ("密码为空", 'admin', '', '密码不能为空！'),
                              ("本地登录", 'admin', '1234567890', '系统管理员'),
                              ("AD登录", 'wjx', 'Admin123', 'weijiaxin有一个超级长的名字')])
    def test_login_csc(self, init, casename, username, password, asserts):
        '''
            测试使用不同的账号密码组合进行登陆测试
        '''
        login_page = LoginPage(self.driver)   # 创建一个登陆页面的实例
        login_page.open()
        login_page.input_username(username)
        login_page.input_password(password)

        if casename == 'AD登录':             # 是否切换Ad域登录
            login_page.switch_usertype()
        login_page.click_submit()

        if login_page.on_page('WinCloud-CSC'):  # 判断登陆情况和tip信息
            login_page.assert_login(asserts)
        else:
            assert login_page.show_msg() == asserts

if __name__ == '__main__':
    pytest.main(['./workspace/testcase/test_login.py'])
