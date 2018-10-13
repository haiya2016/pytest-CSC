# coding=utf-8
'''
    Created on 2018-10-12
    @author: wjx
    Project: 服务管理模块的测试用例
'''

import pytest
from workspace.config.running_config import get_driver
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
        service_page.enter_create()
        az_dict = [
            {
                '可用分区名称': '38KVM',
                '镜像': ['cirros_xen'],
                '配置列表': [('配置1', '1', '1')],
                '应用列表': ['tomcat'],
                '磁盘服务': 'zhh云硬盘服务'
            }
        ]
        input_data = {
            '服务名称': '自动化创建云服务01',
            '服务有效期': '永久',
            '发布范围': '全局',
            '服务图标': '这里输入图标路径',
            '服务SLA登记': 'P1',
            '服务介绍': '这里输入服务的相关介绍内容',
            '计费规则': '计费规则的名称',
            '可用分区': az_dict
        }
        for data in input_data:
            service_page.create_vm_service(data, input_data[data])

    def teardown_method(self):
        """
            在每个测试用例结束后运行，关闭浏览器
        """
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['-q', './workspace/testcase/test_service.py'])
