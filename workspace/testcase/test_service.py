# coding=utf-8
'''
    Created on 2018-10-12
    @author: wjx
    Project: 服务管理模块的测试用例
'''

import time
import pytest
from workspace.config.running_config import get_driver
# from workspace.config import csc_config
from workspace.pages.login_page import LoginPage
from workspace.pages.services_page import ServicesPage


class TestService():
    '''
    服务管理case
    '''

    def setup_method(self):
        """
            初始化，在每个方法前运行
        """
        self.driver = get_driver()
        self.login_driver = LoginPage.login(self.driver)  # 调用LoginPage的类方法，直接获取一个已登录的浏览器

    def test_create_vm(self):
        '''
        创建云主机服务
        '''
        # 使用已登录的浏览器生成一个已登录的云主机创建页面的对象
        service_page = ServicesPage(self.login_driver)
        service_page.enter_menu()
        service_page.create_vm_service()
        time.sleep(5)

    def teardown_method(self):
        """
            在每个测试用例结束后运行，关闭浏览器
        """
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['-q', './workspace/testcase/test_service.py'])
