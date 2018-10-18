# coding=utf-8
'''
@Created on 2018-9-9
@author: wjx
@Project:基础类BasePage，封装所有页面都公用的方法，定义open函数，重定义定位、点击、输入等函数。
WebDriverWait提供了显式等待方式。
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from workspace.config.logging_sys import Logger
from workspace.config import csc_config


class BasePage():
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
        使用title获取当前窗口title，检查输入的title是否在当前title中

        :Args:
         - pagetitle:页面的标题

        Return:
         - 返回比较结果（True 或 False）
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

        :Args:
         - *loc:定位因子，由定位方法和路径组成，因为是元组所以要加星号

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
        except Exception as errmsg:
            self.log.exception(f'定位{loc}时发生异常：{errmsg}')
            raise
        # else:
            # self.log.info(f'查找元素:{loc} 成功！')
        return self.driver.find_element(*loc)

    def click_element(self, *loc):
        '''
        重写元素点击方法，增加是否可点击的判断

        :Args:
         - *loc:定位因子，由定位方法和路径组成，因为是元组所以要加星号

        '''
        self.scroll(*loc)
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc))
        except Exception as errmsg:
            self.log.exception(f'元素{loc}无法点击：{errmsg}')
            raise
        else:
            # self.log.info(f"点击元素{loc}")
            self.find_element(*loc).click()
            # time.sleep(2)  # 点击元素后睡眠2秒等待界面加载


    def switch_frame(self, *loc):
        '''
        重写switch_to_frame方法

        :Args:
         - *loc:定位因子，由定位方法和路径组成，因为是元组所以要加星号

        '''
        self.log.info(f'切换到ifram框架：{loc}')
        return self.driver.switch_to_frame(*loc)

    def assert_by_text(self, text, *loc):
        '''
        判断获取的元素文本是否和预期一致

        :Args:
         - text:用于比较的文本
         - *loc:定位因子

        '''
        assert self.find_element(*loc).text == text

    def select_by_text(self, text, *loc):
        '''
        通过文本对下拉框进行选择

        :Args:
         - text:用于选择的文本
         - *loc:定位因子

        '''
        select = Select(self.find_element(*loc))
        select.select_by_visible_text(text)

    def set_value(self, value, *loc, clear=True):
        '''
        通过文本对下拉框进行选择

        :Args:
         - value:用于输入的文本
         - *loc:定位因子
         - clear:输入前是否清空原数据，默认为true(清空)

        '''
        if clear:
            self.find_element(*loc).clear()
        self.find_element(*loc).send_keys(value)


    def move_and_click(self, *loc, xoffset=200, yoffset=0):
        '''
        移动到指定的元素的某个坐标并点击

        :Args:
         - xoffset:横坐标，默认200
         - yoffset:纵坐标，默认0

        '''
        element = self.find_element(*loc)
        ActionChains(self.driver).move_to_element_with_offset(element, xoffset, yoffset).perform()
        ActionChains(self.driver).click().perform()

    def get_element_count(self, *loc):
        '''
        获取指定元素的个数

        :Args:
         - *loc: 定位因子
        :Return:
         - len(element_list):指定元素的个数
        '''
        element_list = self.driver.find_elements(*loc)
        return len(element_list)

    def get_attribute(self, attribute, *loc):
        '''
        获取元素的attribute属性

        :Args:
         - attribute:元素的某个属性
         - *loc:定位因子

        '''
        return self.find_element(*loc).get_attribute(attribute)


    #################################   js脚本  #########################################

    def script(self, src):
        '''
        定义script方法，用于执行js脚本，范围执行结果

        :Args:
         - src:js脚本，字符串格式

        '''
        self.log.info(f'执行js脚本：{src}')
        self.driver.execute_script(src)

    def scroll(self, *loc):
        '''
        将窗口聚焦到元素对象上（滚动窗口）

        :Args:
         - *loc:定位element对象

        '''
        element = self.find_element(*loc)
        self.driver.execute_script('arguments[0].focus();', element)

    def remove_attribute_by_js(self, attribute, *loc):
        '''
        通过js移除元素的attribute属性

        :Args:
         - attribute:元素的某个属性
         - *loc:定位因子

        '''
        self.log.info(f'移除元素{attribute}属性')
        element = self.find_element(*loc)
        self.driver.execute_script(f"arguments[0].removeAttribute('{attribute}')", element)

    def set_value_by_js(self, value, *loc):
        '''
        通过js直接设置指定元素的值

        :Args:
         - value:需要设置的值
         - *loc:定位因子

        '''
        element = self.find_element(*loc)
        self.driver.execute_script(f"arguments[0].value='{value}'", element)
        self.log.info(f'通过js直接设置{loc}的值:{value}')

    def get_value_by_js(self, *loc):
        '''
        通过js获取指定元素的值

        :Args:
         - *loc:定位因子
        :Return:
         - value:通过js获取到的值

        '''
        element = self.find_element(*loc)
        value = self.driver.execute_script("return arguments[0].value", element)
        self.log.info(f'通过js获取到的值为:{value}')
        return str(value)
