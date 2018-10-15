# coding=utf-8
'''
Created on 2018-9-9
@author: wjx
Project:基础类BasePage，封装所有页面都公用的方法，
定义open函数，重定义find_element，switch_frame，send_keys等函数。
在初始化方法中定义驱动driver，基本url，title
WebDriverWait提供了显式等待方式。
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from workspace.config.logging_sys import Logger
from workspace.config import csc_config


class BasePage(object):
    """
    BasePage封装所有页面都公用的方法，例如driver, url ,FindElement等
    初始化url为配置文件中的url
    """

    def __init__(self, selenium_driver, base_url=csc_config.URL):
        self.driver = selenium_driver
        self.base_url = base_url
        self.log = Logger('基本操作').getlog()

    def on_page(self, pagetitle):
        '''
        使用title获取当前窗口title，检查输入的title是否在当前title中，返回比较结果（True 或 False）
        '''
        return pagetitle in self.driver.title

    def _open(self, url):
        '''
        打开页面，并校验页面链接是否加载正确
        以单下划线_开头的方法，在使用import *时，该方法不会被导入，保证该方法为类私有的。
        '''
        self.driver.get(url)
        # assert self.on_page(pagetitle), "打开开页面失败 %s" %url

    def open(self):
        '''
        定义open方法，调用_open()进行打开链接
        '''
        self.log.info(f'打开页面：{str(self.base_url)}')
        self._open(self.base_url)

    def find_element(self, *loc):
        '''
        重写元素定位方法
        :param *loc:定位因子，由定位方法和路径组成，因为是元组所以要加星号
        :type *loc:元组
        '''
        try:
            # 确保元素是可见的。
            # 注意：入参本身是元组，不需要加*
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(loc))
            # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc))
            # 对定位到的元素进行高亮
            # self.driver.execute_script("arguments[0].style.border='3px solid red'", element)
            # return element
        # except TimeoutException as errmsg:
            # self.log.error(f'定位{loc}超时：{errmsg}', exc_info=True)
        except Exception as allerr:
            self.log.exception(f'定位{loc}时发生异常：{allerr}')
            raise Exception
        # else:
            # self.log.info(f'查找元素:{loc} 成功！')
        return self.driver.find_element(*loc)

    def click_element(self, *loc):
        '''
        重写元素点击方法，增加是否可点击的判断
        '''
        self.scroll(*loc)
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc))
        except Exception as allerr:
            self.log.exception(f'元素{loc}无法点击：{allerr}')
            raise Exception
        else:
            # self.log.info(f"点击元素{loc}")
            self.find_element(*loc).click()
            # time.sleep(2)  # 点击元素后睡眠2秒等待界面加载


    def switch_frame(self, *loc):
        '''
        重写switch_to_frame方法
        '''
        self.log.info(f'切换到ifram框架：{loc}')
        return self.driver.switch_to_frame(*loc)

    def assert_by_text(self, text, *loc):
        '''
        判断获取的元素文本是否和预期一致
        :param text:用于比较的文本
        :param *loc:定位因子
        '''
        assert self.find_element(*loc).text == text

    def select_by_text(self, text, *loc):
        '''
        通过文本对下拉框进行选择
        :param text:用于选择的文本
        :param *loc:定位因子
        '''
        select = Select(self.find_element(*loc))
        select.select_by_visible_text(text)

    def set_value(self, text, *loc):
        '''
        通过文本对下拉框进行选择
        :param text:用于输入的文本
        :param *loc:定位因子
        '''
        self.find_element(*loc).clear()
        self.find_element(*loc).send_keys(text)


    #################################   js脚本  #########################################

    def script(self, src):
        '''
        定义script方法，用于执行js脚本，范围执行结果
        '''
        self.log.info(f'执行js脚本：{src}')
        self.driver.execute_script(src)

    def scroll(self, *loc):
        '''
        element对象的“底端”与当前窗口的“底部”对齐
        :param *loc:定位element对象
        '''
        element = self.find_element(*loc)
        self.driver.execute_script('arguments[0].focus();', element)

    def remove_attribute_by_js(self, attribute, *loc):
        '''
        通过js移除元素的attribute属性
        :param attribute:元素的某个属性
        :param *loc:定位因子
        '''
        self.log.info('移除元素disabled属性，使元素可见')
        element = self.find_element(*loc)
        self.driver.execute_script(f"arguments[0].removeAttribute('{attribute}')", element)

    def set_value_by_js(self, value, *loc):
        '''
        通过js直接设置指定元素的值
        :param value:需要设置的值
        :param *loc:定位因子
        '''
        element = self.find_element(*loc)
        self.driver.execute_script(f"arguments[0].value='{value}'", element)
        self.log.info(f'通过js直接设置{*loc}的值:{value}')
