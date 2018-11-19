'''
@Description: In User Settings Edit
@Author: your name
@Date: 2018-11-13 11:48:42
@LastEditTime: 2018-11-13 17:12:56
@LastEditors: Please set LastEditors
'''
# coding=utf-8


import pytest
from workspace.pages.powerVC.PVC import PowerVC
from workspace.config.running_config import get_driver
from workspace.config import csc_config


class Testpowervc():
    """
        powervc
    """

    def setup_method(self):
        """
            初始化，在每个方法前运行
        """
        self.driver = get_driver()


    def test_create_stroge_model(self):
        '''
            测试使用不同的账号密码组合进行登陆测试
        '''
        pvc = PowerVC(self.driver)   # 创建一个登陆页面的实例
        pvc.get(csc_config.POWERVC)
        pvc.input_username(csc_config.USER_PVC['账号'])
        pvc.input_password(csc_config.USER_PVC['密码'])
        pvc.click_submit()
        pvc.assert_login()
        pvc.enter_config()
        pvc.enter_stroge_model()
        for i in range(13, 30):
            pvc.create_stroge_model(str(i))


    def teardown_method(self):
        """
            在每个测试用例结束后运行，关闭浏览器
        """
        self.driver.quit()
        # pass


if __name__ == '__main__':
    pytest.main(['-q', '--tb=line', './workspace/testcase/test_pvc.py'])
