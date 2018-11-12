# coding=utf-8
'''
@Created on 2018-9-9
@author: wjx
@Project:页面基本操作方法：如input_username，input_password，click_submit
'''

from workspace.config.logging_sys import Logger
from workspace.config import csc_config
from workspace.addin.pageobject import PageElement, PageObject


class LoginPage(PageObject):
    '''
    继承BasePage类
    封装登录页面所需要使用的方法
    '''
    # 定位器，通过元素属性定位元素对象
    userid_loc = PageElement(name='username')
    password_loc = PageElement(name='password')
    submit_loc = PageElement(name='submit')
    usertype_local_loc = PageElement(xpath='//*[@id="userType"]/option[1]')
    usertype_ad_loc = PageElement(id_='adUser')
    msg_loc = PageElement(xpath='//*[@id="cas"]/div/div[1]/div/div[2]/div[2]/div[3]')
    userinfo_loc = PageElement(xpath='//a[@data-bind="click:loadUserInfo"]/span')
    username_loc = PageElement(xpath="//td[text()='昵称']/..//td[2]")

    # 日志
    log = Logger('登录').getlog()

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

    def show_msg(self):
        '''
        用户名或密码不合理时Tip框内容展示
        '''
        mesg = self.msg_loc.text
        self.log.info(f'提示信息：{mesg}')
        return mesg

    def switch_usertype(self):
        '''
        切换为AD用户登陆
        '''
        self.log.info('切换为AD用户登陆')
        self.usertype_ad_loc.click()

    def assert_login(self, username):
        '''
        登录成功页面判断用户id是否相同，登录成功则保存cookie
        '''
        self.userinfo_loc.click()
        show_name = self.username_loc.get_attribute('title')
        assert username == show_name
        self.log.info('登录成功')


    @classmethod
    def login(cls, driver, url=None, user=None):
        '''
        类方法：账号正常登录后返回浏览器给用例使用，默认用管理员账号登录
        '''
        if not url:
            url = csc_config.URL
        if not user:
            user = csc_config.USER_ADMIN
        login = cls(driver)    # 初始化
        login.get(url)
        login.input_username(user['账号'])
        login.input_password(user['密码'])
        if user['类型'] != '本地':
            login.switch_usertype()
        login.click_submit()
        cls.assert_login(login, user['昵称'])
        return login.driver
