'''
@Description: powerVC页面自动化
@Author: wjx
@Date: 2018-11-13 09:36:09
@LastEditTime: 2018-11-13 14:49:33
@LastEditors: Please set LastEditors
'''

from workspace.config.logging_sys import Logger
from workspace.config import csc_config
from workspace.addin.pageobject import PageElement, PageObject


class PowerVC(PageObject):
    '''
    继承BasePage类
    封装登录页面所需要使用的方法
    '''
    # 定位器，通过元素属性定位元素对象
    userid_loc = PageElement(name='username')
    password_loc = PageElement(name='password')
    submit_loc = PageElement(id_='dijit_form_Button_0_label')
    userinfo_loc = PageElement(class_='idxHeaderUserText')
    config_loc = PageElement(id_='olympicsApplication-menuBar-configuration_text')
    st_mode_loc = PageElement(xpath="//a[text()='存储器模板']")
    create_stmode_button = PageElement(xpath="//span[text()='创建']")
    stroge_pool = PageElement(xpath='//div[@aria-label="存储池"]//td[text()="winserver"]')
    stomode_name = PageElement(name='name')
    create_stmode = PageElement(xpath='//td[@class="gridxBarToolBar"]//span[text()="创建"]')


    # 日志
    log = Logger('powerVC').getlog()

    # 操作
    def input_username(self, userid):
        '''
        输入用户id
        '''
        self.log.info(f'{userid}')
        self.userid_loc.send_keys(userid)

    def input_password(self, password):
        '''
        输入密码
        '''
        self.log.info(f'{password}')
        self.password_loc.send_keys(password)

    def click_submit(self):
        '''
        点击登录
        '''
        self.log.info('点击登录按钮')
        self.submit_loc.click()



    def assert_login(self):
        '''
        登录成功页面判断用户id是否相同，登录成功则保存cookie
        '''
        show_name = self.userinfo_loc.text
        assert show_name == 'root (ibm-default)'
        self.log.info('登录成功')

    def enter_config(self):
        '''
        进入配置页面
        '''
        self.config_loc.click()

    def enter_stroge_model(self):
        '''
        进入存储模板页面
        '''
        self.st_mode_loc.click()

    def create_stroge_model(self, name):
        '''
        @msg: 创建存储模板
        @param name 模板名称{str} 
        @return: 
        '''
        self.create_stmode_button.click()
        self.stroge_pool.click()
        self.stomode_name.send_keys(name)
        self.create_stmode.click()
        

