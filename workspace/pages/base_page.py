# coding=utf-8
'''
@Created on 2018-9-9
@author: wjx
@Project:基础类BasePage，封装所有页面都公用的方法，定义open函数，重定义定位、点击、输入等函数。
WebDriverWait提供了显式等待方式。
'''
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from workspace.config import csc_config
from workspace.config.logging_sys import Logger


class BasePage():
    """
    BasePage封装所有页面都公用的方法
    初始化url为配置文件中的url
    """
    breadcrumb_loc = (By.XPATH, "//ul[@class='breadcrumb']//li[@class='active']")   #  面包屑地址
    local_org_loc = (By.XPATH, "//span[@class='node_name' and text()='本地组织']")   #  用户选择，本地组织节点
    ad_org_loc = (By.XPATH, "//span[@class='node_name' and text()='AD域组织']")     #  用户选择，AD域组织节点
    userid_search_loc = (By.XPATH, "//span[text()='账号']/../input")                #  用户选择，账号搜索框
    username_search_loc = (By.XPATH, "//span[text()='昵称']/../input")              #  用户选择，昵称搜索框
    search_button_loc = (By.XPATH, "//button[text()='搜索']")                       #  搜索按钮
    add_user_loc = (By.XPATH, "//button[@data-bind='click: saveUsers']")            #  用户选择，确认按钮


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


    def enter_menu(self, menu_name, role='系统管理员'):
        '''
        进入指定的菜单

        :Args:
         - menu_name:菜单名称，可以为子菜单名称
         - role:角色，用于确认具体菜单内容，默认为系统管理员
        '''
        found = False
        menu_tree = csc_config.MEMU_TREE[role]  #  从配置文件读取指定角色的菜单
        if menu_name in menu_tree:  #  判断一级菜单
            self.click_element(By.XPATH, f"//ul[@id='menuListId']//span[text()='{menu_name}']")
            found = True
        else:
            for menu in menu_tree:
                if menu_name in menu_tree[menu]:   #  判断二级菜单
                    self.click_element(By.XPATH, f"//ul[@id='menuListId']//span[text()='{menu}']")
                    self.click_element(By.XPATH, f"//ul[@id='menuListId']//span[text()='{menu_name}']")
                    found = True
        if found:   #  判断输入的菜单是否在配置中
            value = self.get_attribute('class', By.XPATH, f"//ul[@id='menuListId']//span[text()='{menu_name}']/../..")
            assert value == 'highlight'  #  判断菜单是否高亮
            if menu_name not in ('首页', '用户管理'):
                self.assert_by_text(menu_name, *self.breadcrumb_loc)   #  判断面包屑地址(首页和用户管理没有面包屑地址)
            self.log.info(f'进入{menu_name}菜单')
        else:
            self.log.error(f"菜单名称{menu_name}不正确")

    def select_user(self, usertype='本地', userid='admin'):
        '''
        通过用户名或者用户昵称选择用户

        :Args:
         - usertype:账号类型，'本地'或者'AD'
         - userid:用户id
         - username:用户昵称
        '''
        if usertype == '本地':
            self.click_element(*self.local_org_loc)
        else:
            self.click_element(*self.ad_org_loc)
        self.set_value(userid, *self.userid_search_loc)
        self.click_element(*self.search_button_loc)
        self.click_element(By.XPATH, f"//td[@title='{userid}']/..//span")  #  在搜索结果中进行勾选
        self.click_element(*self.add_user_loc)



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
        try:
            select.select_by_visible_text(text)
        except NoSuchElementException as errmsg:
            self.log.exception(f'下拉列表中没有{text}选项：{errmsg}')


    def set_value(self, value, *loc, clear=True):
        '''
        对文本框进行输入

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

        :Returns:
         - 返回元素的属性

        '''
        return self.find_element(*loc).get_attribute(attribute)


    def get_role(self):
        '''
        通过接口获取当前用户登陆的角色

        :Returns:
         - response.json()['roleName']，接口返回数据中的rolename字段
        '''
        cookie_items = self.driver.get_cookies()
        cookies = {}   # 定义一个空的字典，存放cookies内容
        for cookie_item in cookie_items:
            cookies[cookie_item['name']] = cookie_item['value']
        response = requests.get(url=csc_config.GET_USER_ROLE, cookies=cookies, verify=False)
        return response.json()['roleName']


    #################################   js脚本  #########################################

    def script(self, src):
        '''
        定义script方法，用于执行js脚本，范围执行结果

        :Args:
         - src:js脚本，字符串格式

        '''
        self.driver.execute_script(src)
        self.log.info(f'执行js脚本：{src}')

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
