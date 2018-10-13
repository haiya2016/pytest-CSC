# coding=utf-8
'''
    Created on 2018-9-9
    @author: wjx
    Project: 资源实例模块的测试用例
'''

import time
import pytest
from workspace.config.running_config import get_driver
# from workspace.config import csc_config
from workspace.pages.login_page import LoginPage
from workspace.pages.vm_create_page import VmCreatePage


class TestCreateVM():
    '''
    创建云主机case
    '''

    def setup_method(self):
        """
            初始化，在每个方法前运行
        """
        self.driver = get_driver()
        self.login_driver = LoginPage.login(self.driver)  # 调用LoginPage的类方法，直接获取一个已登录的浏览器

    def test_create_vm(self):
        '''
        创建云主机
        '''
        # 使用已登录的浏览器生成一个已登录的云主机创建页面的对象
        vm_page = VmCreatePage(self.login_driver)
        vm_page.enter_menu()
        # 设置需要填写的值
        input_data = {
            '云主机名称': 'python01',
            'VM Name': 'python01',
            'Hostname': 'python01',
            '归属服务': 'wpl',
            '归属VDC': 'zhhvdca',
            '归属用户': 'admin',
            '业务系统': '',
            '应用集群': '',
            '到期时间': '2019-01-01',
            '备注': '自动化创建的云主机',
            '可用分区': 'AZ-Winserver 虚拟化:WinServer',
            '镜像': 'win2012',
            '宿主机': '192.168.206.76',
            '存储池': 'Local storage(192.168.206.76)',
            'CPU': '1',
            '内存': '1',
            '系统盘': '',
            'IP池': '208',
        }
        for data in input_data:
            vm_page.input_item(data, input_data[data])
            # time.sleep(2)
        time.sleep(5)

    def teardown_method(self):
        """
            在每个测试用例结束后运行，关闭浏览器
        """
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['-q', './workspace/testcase/test_create_vm.py'])
