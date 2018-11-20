'''
@Description: 
@Author: wjx
@Date: 2018-10-12 09:18:59
@LastEditors: wjx
@LastEditTime: 2018-11-20 16:03:42
'''
# coding=utf-8


import pytest

from workspace.config.running_config import get_driver
from workspace.pages.login_page import LoginPage
from workspace.pages.services_page import ServicesPage


class TestService():
    '''
    服务管理case
    '''

    @pytest.fixture(scope='function')
    def init(self):
        '''
        获取和退出浏览器
        '''
        self.driver = get_driver()
        self.login_driver = LoginPage.login(self.driver)  # 调用LoginPage的类方法，直接获取一个已登录的浏览器
        yield
        self.driver.quit()

    def test_create_vm(self, init):
        '''
        创建云主机服务
        '''
        # 使用已登录的浏览器生成一个已登录的云主机创建页面的对象
        service_page = ServicesPage(self.login_driver)
        service_page.enter_create()
        az_list = [
            {
                '可用分区名称': '38KVM',
                '镜像': ['cirros_xen'],
                '配置列表': [('配置1', '1', '1')],
                '应用列表': ['tomcat'],
                '磁盘服务': 'zhh云硬盘服务'
            },
            {
                '可用分区名称': 'hmc',
                '镜像': ['AIX5_3'],
                '配置列表': [('配置1', '1', '1')],
                '磁盘服务': '云硬盘服务-wangzd'
            }
        ]
        input_data = {
            '服务名称': '自动化创建云服务04-python',
            '服务有效期': '永久',
            '发布范围': '全局',
            '服务图标': '这里输入图标路径',
            '服务SLA等级': 'P3',
            '服务介绍': '该云主机服务由python自动化脚本执行发布',
            '计费规则': ['auto', '内存'],
            '可用分区': az_list
        }
        for data in input_data:
            service_page.create_vm_service(data, input_data[data])
        service_page.save_and_release()


if __name__ == '__main__':
    pytest.main(['-q', './workspace/testcase/test_service.py'])
