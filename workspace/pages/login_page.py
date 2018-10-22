# coding=utf-8
'''
@Created on 2018-9-9
@author: wjx
@Project:页面基本操作方法：如input_username，input_password，click_submit
'''
from selenium.webdriver.common.by import By
from workspace.pages.base_page import BasePage
from workspace.config.logging_sys import Logger
from workspace.config import csc_config


class LoginPage(BasePage):
    '''
    继承BasePage类
    封装登录页面所需要使用的方法
    '''
    # 定位器，通过元素属性定位元素对象
    username_loc = (By.NAME, 'username')
    password_loc = (By.NAME, 'password')
    submit_loc = (By.NAME, 'submit')
    usertype_local_loc = (By.XPATH, '//*[@id="userType"]/option[1]')
    usertype_ad_loc = (By.ID, 'adUser')
    msg_loc = (By.XPATH, '//*[@id="cas"]/div/div[1]/div/div[2]/div[2]/div[3]')
    userid_loc = (By.XPATH, '//*[@id="header"]/div[2]/ul/li[5]/a/span')

    # 日志
    log = Logger('登录').getlog()

    # 操作
    def input_username(self, username):
        '''
        输入用户名
        '''
        self.log.info(f'{username}')
        self.set_value(username, *self.username_loc)

    def input_password(self, password):
        '''
        输入密码
        '''
        self.log.info(f'{password}')
        self.set_value(password, *self.password_loc)

    def click_submit(self):
        '''
        点击登录
        '''
        self.log.info('点击登录按钮')
        self.click_element(*self.submit_loc)

    def show_msg(self):
        '''
        用户名或密码不合理时Tip框内容展示
        '''
        mesg = self.find_element(*self.msg_loc).text
        self.log.info(f'提示信息：{mesg}')
        return mesg

    def switch_usertype(self):
        '''
        切换为AD用户登陆
        '''
        self.log.info('切换为AD用户登陆')
        self.click_element(*self.usertype_ad_loc)
        # self.find_element(*self.usertype_ad_loc).click()

    def assert_login(self, username):
        '''
        登录成功页面判断用户id是否相同，登录成功则保存cookie
        '''
        self.assert_by_text(username, *self.userid_loc)
        self.log.info('登录成功')
        self.save_cookie()


    @classmethod
    def login(cls, driver, url=None, user=None):
        '''
        类方法：账号正常登录后返回浏览器给用例使用，默认用管理员账号登录
        '''
        if not url:
            url = csc_config.URL
        if not user:
            user = csc_config.USER_ADMIN
        login = cls(driver, url)    # 初始化
        login.open()
        login.input_username(user['账号'])
        login.input_password(user['密码'])
        if user['类型'] != '本地':
            login.switch_usertype()
        login.click_submit()
        cls.assert_login(login, user['昵称'])
        return login.driver
