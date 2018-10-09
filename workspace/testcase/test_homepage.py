# coding=utf-8
'''
    Created on 2018-9-9
    @author: wjx
    Project: 首页模块的测试用例
'''
import pytest
from workspace.config.running_config import get_driver
from workspace.config import csc_config
from workspace.pages.login_page import LoginPage
from workspace.pages.home_page import HomePage


class TestHomepageCSC():
    '''
        CSC首页case
    '''

    def setup_method(self):
        """
            初始化，在每个方法前运行
        """
        self.driver = get_driver()
        self.login_driver = LoginPage.login(self.driver)
        self.database = csc_config.DB

    def test_switch_dc(self):
        '''
            切换数据中心
        '''
        homepage = HomePage(self.login_driver)
        homepage.dc_select('opws')   # 选择某个数据中心的数据
        print(homepage.dc_check())
        print(homepage.db_check(self.database, 'opws'))

    def teardown_method(self):
        """
            在每个测试用例结束后运行，关闭浏览器
        """
        self.driver.quit()
        self.database.close()


if __name__ == '__main__':
    pytest.main(['-q', './workspace/testcase/test_homepage.py'])
