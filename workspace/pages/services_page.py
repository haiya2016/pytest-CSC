# coding=utf-8
'''
    Created on 2018-10-09
    @author: wjx
    Project:服务管理页面
'''

from selenium.webdriver.common.by import By
from workspace.pages.base_page import BasePage
from workspace.config.logging_sys import Logger


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

    # 添加可用分区
    azTab_loc = (By.XPATH, "//a[@href='#resources']")                                       #  云主机服务创建-可用分区tab
    addAZ_loc = (By.XPATH, "//*[@id='resources']/h5/a/button")                              #  云主机服务创建-可用分区添加按钮
    azNameSearch_loc = (By.XPATH, "//span[text()='可用分区名称']/../input")                 #  添加可用分区-可用分区搜索框
    azCancle_loc = (By.XPATH, "//h2[text()='添加可用分区']/../..//button[text()='取消']")   #  添加可用分区-取消按钮
    azConfirm_loc = (By.XPATH, "//h2[text()='添加可用分区']/../..//button[text()='确认']")  #  添加可用分区-确认按钮

    addImage_loc = None#  云主机服务创建-添加镜像按钮
    osTypeSelect_loc = (By.XPATH, "//span[text()='操作系统类型']/../select")                #  添加镜像-操作系统类型下拉框
    osNameSearch_loc = (By.XPATH, "//span[text()='操作系统名称']/../input")                 #  添加镜像-操作系统名称搜索框
    imageNameSearch_loc = (By.XPATH, "//span[text()='镜像名称']/../input")                  #  添加镜像-镜像名称搜索框
    imageCancle_loc = (By.XPATH, "//h2[text()='添加镜像']/../..//button[text()='取消']")    #  添加镜像-取消按钮
    imageConfirm_loc = (By.XPATH, "//h2[text()='添加镜像']/../..//button[text()='确认']")   #  添加镜像-确认按钮

    configCPU_loc = None       #  添加可用配置-CPU
    configTitle_loc = None    #  添加可用配置-标题
    configMem_loc = None    #  添加可用配置-内存
    addConfig_loc = None #  添加可用配置-添加按钮

    addSoft_loc = None                     #  云主机服务创建-添加应用按钮
    osTypeSearch_loc = None #  添加应用-操作系统类型搜索框
    softCancle_loc = (By.XPATH, "//h2[text()='添加应用']/../..//button[text()='取消']")                         #  添加应用-取消按钮
    softConfirm_loc = (By.XPATH, "//h2[text()='添加应用']/../..//button[text()='确认']")                        #  添加应用-确认按钮
    softTypeSelect_loc = (By.XPATH, "//span[text()='软件类型']/../select")                                      #  添加应用-软件类型下拉框
    softNameSearch_loc = (By.XPATH, "//span[text()='软件名称']/../input")                                       #  添加应用-软件名称搜索框

    cancleButton_loc = (By.XPATH, "//div[3]/div[1]/a")                              #  云主机服务创建-取消按钮（顶部）
    saveButton_loc = (By.XPATH, "//div[3]/div[1]/button[text()='保存']")            #  云主机服务创建-保存按钮（顶部）
    releaseButton_loc = (By.XPATH, "//div[3]/div[1]/button[text()='保存并发布']")    #  云主机服务创建-保存并发布按钮（顶部）

    diskTab_loc = (By.XPATH, "//a[@href='#basic']")                                 #  云主机服务创建-磁盘服务tab
    vmTab_loc = (By.XPATH, "//a[@href='#resources']")
    diskservice_loc = None             #  磁盘服务下拉框

    def refash_loc(self, az_name):
        '''刷新页面元素定位'''
        self.addImage_loc = (By.XPATH, f"//label[text()='{az_name}']/../../..//a[text()='+添加镜像 ']")#  云主机服务创建-添加镜像按钮
        self.configCPU_loc = (By.XPATH, f"//label[text()='{az_name}']/../../..//select[@data-bind='value: configCpu']")       #  添加可用配置-CPU
        self.configTitle_loc = (By.XPATH, f"//label[text()='{az_name}']/../../..//input[@data-bind='value: configTitle']")    #  添加可用配置-标题
        self.configMem_loc = (By.XPATH, f"//label[text()='{az_name}']/../../..//select[@data-bind='value: configMemory']")    #  添加可用配置-内存
        self.addConfig_loc = (By.XPATH, f"//label[text()='{az_name}']/../../..//button[@data-bind='click: $root.addConfig']") #  添加可用配置-添加按钮
        self.addSoft_loc = (By.XPATH, f"//label[text()='{az_name}']/../../..//a[text()='+添加应用']")                     #  云主机服务创建-添加应用按钮
        self.osTypeSearch_loc = (By.XPATH, f"//label[text()='{az_name}']/../../..//span[text()='操作系统类型']/../input") #  添加应用-操作系统类型搜索框
        self.diskservice_loc = (By.XPATH, f"//td[text()='{az_name}']/..//select")             #  磁盘服务下拉框

    def enter_menu(self):
        '''
        进入服务管理菜单
        '''
        self.click_element(*self.serviceMenu_loc)
        self.log.info('进入服务管理菜单')

    def enter_create(self):
        '''
        进入创建服务页面
        '''
        self.log.info('点击创建按钮')
        self.click_element(*self.serviceCreate_loc)  # 点击创建按钮

    def create_vm_service(self, item_type, item_value):
        '''
        创建云主机服务
        '''
        # TODO:服务截止日期暂时只能选择永久，无法选择具体日期，需要开发修改页面样式
        self.log.info(f"对数据进行处理：{item_type}: {item_value}")
        if item_type in ['服务SLA等级', 'CPU', '内存']:
            self.item_select(item_type, item_value)
        if item_type in ['服务名称', '服务介绍']:
            self.item_typing(item_type, item_value)
        if item_type == '发布范围':
            if item_value == '全局':
                self.click_element(*self.overRelease_loc)
        if item_type == '可用分区':
            for item in item_value:
                self.az_process(item)


    def az_process(self, item_dict):
        '''
        对可用分区的数据进行处理
        '''
        self.click_element(*self.addAZ_loc)  # 点击可用分区添加按钮
        for item in item_dict:
            if item == '可用分区名称':
                az_name = item_dict['可用分区名称']
                self.refash_loc(az_name)
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
                self.script("window.scrollTo(0, 300)")
                self.click_element(*self.diskTab_loc)    # TODO:点击不到
                self.selectByText(item_dict['磁盘服务'], *self.diskservice_loc)
                self.click_element(*self.vmTab_loc)

    def add_az(self, azName):
        '''
        查找病添加可用分区
        '''
        self.sendKeys(azName, *self.azNameSearch_loc)
        self.click_element(*self.searchButton_loc)
        self.click_element(*self.firstResult_loc)
        self.click_element(*self.azConfirm_loc)

    def add_iamge(self, imageName):
        '''
        查找并添加镜像
        '''
        self.log.info(f"添加镜像{imageName}")
        # self.scroll(*self.addImage_loc)
        self.click_element(*self.addImage_loc)
        self.sendKeys(imageName, *self.imageNameSearch_loc)
        self.click_element(*self.searchButton_loc)
        self.click_element(*self.firstResult_loc)
        self.click_element(*self.imageConfirm_loc)

    def add_config(self, config):
        '''
        添加配置
        '''
        self.log.info(f"添加配置{config}")
        self.sendKeys(config[0], *self.configTitle_loc)
        self.selectByText(config[1], *self.configCPU_loc)
        self.selectByText(config[2], *self.configMem_loc)
        self.click_element(*self.addConfig_loc)

    def add_soft(self, soft):
        '''
        添加应用
        '''
        self.log.info(f"添加应用{soft}")
        self.click_element(*self.addSoft_loc)
        self.sendKeys(soft, *self.softNameSearch_loc)
        self.click_element(*self.searchButton_loc)
        self.click_element(*self.firstResult_loc)
        self.click_element(*self.softConfirm_loc)

    def item_select(self, item_type, item_value):
        '''
        处理所有下拉框
        :param item_type:下拉框的名称
        :param item_value:下拉框的文本内容
        '''
        if item_type == '服务SLA等级':
            self.selectByText(item_value, *self.SLAselect_loc)
        elif item_type == 'CPU':
            self.selectByText(item_value, *self.configCPU_loc)
        elif item_type == '内存':
            self.selectByText(item_value, *self.configMem_loc)

    def item_typing(self, item_type, item_value):
        '''
        处理所有输入框
        :param item_type:输入框的名称
        :param item_value:输入框的文本内容
        '''
        if item_type == '服务名称':
            self.sendKeys(item_value, *self.serviceName_loc)
        elif item_type == '服务介绍':
            self.sendKeys(item_value, *self.serviceDesc_loc)