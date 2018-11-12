# coding=utf-8
'''
@Created on 2018-10-09
@author: wjx
@Project:服务管理页面
'''
import time

from selenium.webdriver.common.by import By

from workspace.config.logging_sys import Logger
# from selenium.webdriver.common.keys import Keys
from workspace.pages.base_page import BasePage


class ServicesPage(BasePage):
    """
    服务管理页面
    """

    # 日志
    log = Logger('服务管理').getlog()

    # 定位因子
    serviceMenu_loc = (By.XPATH, "//ul[@id='menuListId']//span[text()='服务管理']")  # 服务管理菜单入口
    breadcrumb_loc = (By.XPATH, "//ul[@class='breadcrumb']//li[@class='active']")   # 面包屑地址
    addDir_loc = (By.XPATH, "//div[@class='widget-buttons']/span[1]")               # 服务目录创建按钮
    delDir_loc = (By.XPATH, "//div[@class='widget-buttons']/span[2]")               # 服务目录删除按钮
    editDir_loc = (By.XPATH, "//div[@class='widget-buttons']/span[3]")              # 服务目录编辑按钮
    serviceDir_loc = (By.XPATH, "//label[@class='widget-caption']/strong")          # 服务目录标题
    serviceType_loc = (By.XPATH, "//span[@class='widget-caption']/span")            # 服务类型
    serviceCreate_loc = (By.XPATH, "//a[text()='创建服务 ']")                        # 创建服务按钮
    serviceStatus_loc = (By.XPATH, "//span[text()='服务状态']/../select")            # 服务状态下拉框
    serviceSearch_loc = (By.XPATH, "//span[text()='服务名称']/../input")             # 服务名称搜索框
    firstResult_loc = (By.XPATH, "//tbody/tr[2]/td[1]/div/label/span")              #  公用-第一个搜索结果
    searchButton_loc = (By.XPATH, "//button[text()='搜索']")                        #  公用-搜索按钮
    resetButton_loc = (By.XPATH, "//button[text()='重置']")                         #  公用-重置按钮

    # 创建云主机服务
    vmDir_loc = (By.XPATH, "//label[text()='云主机']")                              #  服务目录-云主机
    serviceName_loc = (By.XPATH, "//label[text()='服务名称：']/..//input")          #  云主机服务创建-服务名称
    SLAselect_loc = (By.XPATH, "//label[text()='服务SLA等级：']/..//select")        #  云主机服务创建-服务SLA等级下拉框
    serviceDesc_loc = (By.XPATH, "//textarea[@id='serviceDesc']")                  #  云主机服务创建-服务介绍
    overRelease_loc = (By.XPATH, "//span[text()='全局发布']")                       #  云主机服务创建-全局发布按钮
    forever_loc = (By.XPATH, "//span[text()='永久']")                               #  截止时间为永久
    deadline_loc = (By.CSS_SELECTOR, "div.col-sm-4.no-padding>div>label>span.text>::before") #  截止时间按钮
    deadlinetime_loc = (By.XPATH, "//input[@id='rangeTime']")                       #  截止时间输入框
    charging_bind_loc = (By.XPATH, "//button[text()='绑定']")                          #  计费规则绑定按钮
    charging_name_loc = None                                                          #  计费规则名称
    chargingConfirm_loc = (By.XPATH, "//h2[text()='绑定计费规则']/../..//button[text()='确认']")       #  计费规则-确认按钮
    chargingcancel_loc = (By.XPATH, "//h2[text()='绑定计费规则']/../..//button[text()='取消']")       #  计费规则-确认按钮

    # 添加可用分区
    azTab_loc = (By.XPATH, "//a[@href='#resources']")                                       #  云主机服务创建-可用分区tab
    addAZ_loc = (By.XPATH, "//*[@id='resources']/h5/a/button")                              #  云主机服务创建-可用分区添加按钮
    azNameSearch_loc = (By.XPATH, "//span[text()='可用分区名称']/../input")                  #  添加可用分区-可用分区搜索框
    azCancle_loc = (By.XPATH, "//h2[text()='添加可用分区']/../..//button[text()='取消']")    #  添加可用分区-取消按钮
    azConfirm_loc = (By.XPATH, "//h2[text()='添加可用分区']/../..//button[text()='确认']")   #  添加可用分区-确认按钮
    osTypeSelect_loc = (By.XPATH, "//span[text()='操作系统类型']/../select")                 #  添加镜像-操作系统类型下拉框
    osNameSearch_loc = (By.XPATH, "//span[text()='操作系统名称']/../input")                  #  添加镜像-操作系统名称搜索框
    imageNameSearch_loc = (By.XPATH, "//span[text()='镜像名称']/../input")                  #  添加镜像-镜像名称搜索框
    imageCancle_loc = (By.XPATH, "//h2[text()='添加镜像']/../..//button[text()='取消']")     #  添加镜像-取消按钮
    imageConfirm_loc = (By.XPATH, "//h2[text()='添加镜像']/../..//button[text()='确认']")    #  添加镜像-确认按钮

    add_image_loc = None         #  云主机服务创建-添加镜像按钮
    config_cpu_loc = None        #  添加可用配置-CPU
    config_title_loc = None      #  添加可用配置-标题
    config_mem_loc = None        #  添加可用配置-内存
    add_config_loc = None        #  添加可用配置-添加按钮
    add_soft_loc = None          #  云主机服务创建-添加应用按钮
    ostype_search_loc = None     #  添加应用-操作系统类型搜索框
    diskservice_loc = None      #  磁盘服务下拉框

    softCancle_loc = (By.XPATH, "//h2[text()='添加应用']/../..//button[text()='取消']")        #  添加应用-取消按钮
    softConfirm_loc = (By.XPATH, "//h2[text()='添加应用']/../..//button[text()='确认']")       #  添加应用-确认按钮
    softTypeSelect_loc = (By.XPATH, "//span[text()='软件类型']/../select")                     #  添加应用-软件类型下拉框
    softNameSearch_loc = (By.XPATH, "//span[text()='软件名称']/../input")                      #  添加应用-软件名称搜索框

    cancleButton_loc = (By.XPATH, "//div[3]/div[1]/a")                              #  云主机服务创建-取消按钮（顶部）
    saveButton_loc = (By.XPATH, "//div[3]/div[1]/button[text()='保存']")            #  云主机服务创建-保存按钮（顶部）
    releaseButton_loc = (By.XPATH, "//div[3]/div[1]/button[text()='保存并发布']")    #  云主机服务创建-保存并发布按钮（顶部）

    diskTab_loc = (By.XPATH, "//a[@href='#basic']")                                 #  云主机服务创建-磁盘服务tab
    sys_info_loc = (By.XPATH, "//h4[text()='系统信息']/../../div[2]")                #  系统消息
    comfirmButton_loc = (By.XPATH, "//button[text()='确定']")                        #  系统消息-确定按钮

    a_loc = (By.XPATH, '//*[@id="page-content"]/div[3]/div[2]/div[1]/div[1]/div/form[1]/div[2]/div[2]/div/label/input')

    def _uptdate_charge_loc(self, charge_name):
        '''
        私有方法，用于根据计费规则名称更新对应计费规则的元素定位
        '''
        self.charging_name_loc = (By.XPATH, f"//td[@title='{charge_name}']/..//span")    #  计费规则名称

    def _update_loc(self, az_name):
        '''
        私有方法，用于刷新可用分区相关的页面元素定位
        :Args:
         - az_name：可用分区的名称
        '''
        path = f"//label[text()='{az_name}']/../../..//"
        self.add_image_loc = (By.XPATH, f"{path}a[text()='+添加镜像 ']")                         #  云主机服务创建-添加镜像按钮
        self.config_cpu_loc = (By.XPATH, f"{path}select[@data-bind='value: configCpu']")       #  添加可用配置-CPU
        self.config_title_loc = (By.XPATH, f"{path}input[@data-bind='value: configTitle']")    #  添加可用配置-标题
        self.config_mem_loc = (By.XPATH, f"{path}select[@data-bind='value: configMemory']")    #  添加可用配置-内存
        self.add_config_loc = (By.XPATH, f"{path}button[@data-bind='click: $root.addConfig']") #  添加可用配置-添加按钮
        self.add_soft_loc = (By.XPATH, f"{path}a[text()='+添加应用']")                           #  云主机服务创建-添加应用按钮
        self.ostype_search_loc = (By.XPATH, f"{path}span[text()='操作系统类型']/../input")       #  添加应用-操作系统类型搜索框
        self.diskservice_loc = (By.XPATH, f"//td[text()='{az_name}']/..//select")               #  磁盘服务下拉框


    def enter_create(self):
        '''
        进入创建服务页面
        '''
        self.enter_menu('服务管理')
        self.click_element(*self.serviceCreate_loc)  # 点击创建按钮
        self.log.info('点击创建按钮')


    def save_and_release(self):
        '''
        保存并发布
        '''
        self.click_element(*self.releaseButton_loc)
        self.assert_by_text("保存并发布成功！", *self.sys_info_loc)
        self.log.info("发布服务成功！")
        self.click_element(*self.comfirmButton_loc)

    def create_vm_service(self, item_type, item_value):
        '''
        创建云主机服务
        :Args:
         - item_type：参数类型
         - item_value：参数值
        '''
        # TODO:服务截止日期暂时只能选择永久，无法选择具体日期，需要开发修改页面样式
        self.log.info(f"对数据进行处理：{item_type}: {item_value}")
        if item_type in ['服务SLA等级', 'CPU', '内存']:
            self.item_select(item_type, item_value)
        if item_type in ['服务名称', '服务介绍']:
            self.item_typing(item_type, item_value)
        if item_type == '服务有效期':
            self.move_and_click(*self.forever_loc)
            time.sleep(5)
        if item_type == '发布范围':
            if item_value == '全局':
                self.click_element(*self.overRelease_loc)
        if item_type == '可用分区':
            for item in item_value:
                self.az_process(item)
        if item_type == '计费规则':
            self.click_element(*self.charging_bind_loc)
            for item in item_value:
                self.charge_process(item)
            self.click_element(*self.chargingConfirm_loc)




    def az_process(self, item_dict):
        '''
        对可用分区的数据进行处理
        '''
        self.click_element(*self.addAZ_loc)  # 点击可用分区添加按钮
        for item in item_dict:
            if item == '可用分区名称':
                az_name = item_dict['可用分区名称']
                self._update_loc(az_name)
                self.add_az(az_name)
            if item == '镜像':
                for imagename in item_dict['镜像']:
                    self.add_iamge(imagename)
            if item == '配置列表':
                for config in item_dict['配置列表']:
                    self.add_config(config)
            if item == '应用列表':
                for soft in item_dict['应用列表']:
                    self.add_soft(soft)
            if item == '磁盘服务':
                self.script("window.scrollTo(0, 300)")      #  滚动到tab可见的位置
                time.sleep(2)
                self.click_element(*self.diskTab_loc)
                self.select_by_text(item_dict['磁盘服务'], *self.diskservice_loc)
                self.click_element(*self.azTab_loc)         #  切换回可用分区tab

    def add_az(self, az_name):
        '''
        查找病添加可用分区
        :Args:
         - az_name：可用分区的名称
        '''
        self.set_value(az_name, *self.azNameSearch_loc)
        self.search_first_result()
        self.click_element(*self.azConfirm_loc)

    def add_iamge(self, image_name):
        '''
        查找并添加镜像
        :Args:
         - image_name：镜像名称
        '''
        self.log.info(f"添加镜像: {image_name}")
        # self.scroll(*self.add_image_loc)
        self.click_element(*self.add_image_loc)
        self.set_value(image_name, *self.imageNameSearch_loc)
        self.search_first_result()
        self.click_element(*self.imageConfirm_loc)

    def add_config(self, config):
        '''
        添加配置
        :Args:
         - config：配置，格式为列表
        '''
        self.log.info(f"添加配置: {config}")
        self.set_value(config[0], *self.config_title_loc)
        self.select_by_text(config[1], *self.config_cpu_loc)
        self.select_by_text(config[2], *self.config_mem_loc)
        self.click_element(*self.add_config_loc)

    def add_soft(self, soft):
        '''
        添加应用
        :Args:
         - soft：软件名称
        '''
        self.log.info(f"添加应用: {soft}")
        self.click_element(*self.add_soft_loc)
        self.set_value(soft, *self.softNameSearch_loc)
        self.search_first_result()
        self.click_element(*self.softConfirm_loc)

    def item_select(self, item_type, item_value):
        '''
        处理所有下拉框
        :Args:
         - item_type:下拉框的名称
         - item_value:下拉框的文本内容
        '''
        if item_type == '服务SLA等级':
            self.select_by_text(item_value, *self.SLAselect_loc)
        elif item_type == 'CPU':
            self.select_by_text(item_value, *self.config_cpu_loc)
        elif item_type == '内存':
            self.select_by_text(item_value, *self.config_mem_loc)

    def item_typing(self, item_type, item_value):
        '''
        处理所有输入框
        :Args:
         - item_type:输入框的名称
         - item_value:输入框的文本内容
        '''
        if item_type == '服务名称':
            self.set_value(item_value, *self.serviceName_loc)
        elif item_type == '服务介绍':
            self.set_value(item_value, *self.serviceDesc_loc)


    def charge_process(self, charge_name):
        '''
        用于勾选计费规则

        :Args:
         - charge_name：计费规则名称

        '''
        self._uptdate_charge_loc(charge_name)
        self.click_element(*self.charging_name_loc)

    def search_first_result(self):
        '''
        点击搜索，勾选第一个结果
        '''
        self.click_element(*self.searchButton_loc)
        self.click_element(*self.firstResult_loc)
