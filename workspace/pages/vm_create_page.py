# coding=utf-8
'''
@Created on 2018-9-9
@author: wjx
@Project:云主机创建页面
'''

from selenium.webdriver.common.by import By
from workspace.pages.base_page import BasePage
from workspace.config.logging_sys import Logger



class VmCreatePage(BasePage):
    '''
    继承BasePage类
    '''
    # 创建日志
    vclog = Logger('云主机创建').getlog()

    # 菜单入口
    virtual_recourse_manage_loc = (By.XPATH, "//ul[@id='menuListId']//span[text()='虚拟化资源管理']")  # 虚拟化资源管理菜单
    recourse_instance_loc = (By.XPATH, "//ul[@id='menuListId']//span[text()='资源实例']")   # 资源实例菜单
    create_button_lov = (By.XPATH, "//div[@id='partition_vms']//a[text()='创建 ']")        # 云主机创建按钮

    # 按钮
    return_button1_loc = (By.XPATH, "//div[1]/a/button")                        # 顶部返回按钮
    return_button2_loc = (By.XPATH, "//div[2]/a/button")                        # 底部返回按钮
    submit_button_loc = (By.XPATH, "//button[text()='立即执行']")                # 立即执行按钮
    confirm_button_loc = (By.XPATH, "//button[@data-bind='click: submit']")     # 提交确认按钮
    search_button_loc = (By.XPATH, "//*[text()='搜索']")                         # 搜索按钮
    reset_button_loc = (By.XPATH, "//*[text()='重置']")                          # 重置按钮
    first_search_result_loc = (By.XPATH, "//table//tr[2]/td[1]//span")           # 所有搜索的第一个结果

    # 基本信息
    name_input_loc = (By.XPATH, "//label[text()='云主机名称：']//..//input")
    vmname_input_loc = (By.XPATH, "//label[text()='VM Name：']//..//input")
    hostname_input_loc = (By.XPATH, "//form/div[2]/div[3]/div/div/input")
    service_loc = (By.XPATH, "//button[@data-bind='click: addService']")
    vdc_loc = (By.XPATH, "//button[@data-bind='click: addVdc']")
    user_loc = (By.XPATH, "//button[@data-bind='click: showUser']")
    bussys_loc = (By.XPATH, "//button[@data-bind='click: $root.addBusSys']")
    busitem_loc = (By.XPATH, "//button[@data-bind='click: $root.addBusItem']")
    applytime_forever_loc = (By.XPATH, "//*[@id='inlineRadio1']//..//span")
    applytime_time_loc = (By.XPATH, "//*[@id='inlineRadio2']//..//span")
    applytime_timefor_loc = (By.ID, 'resource_instance_vm_limit_option2_unit')
    applytime_date_loc = (By.XPATH, "//*[@id='inlineRadio3']//..//span")
    applytime_datefor_loc = (By.ID, 'resource_instance_vm_limit_option3')
    textarea_input_loc = (By.XPATH, "//textarea")                               # 备注
    # 配置信息
    az_loc = (By.XPATH, "//label[text()='可用分区：']/..//select")
    image_loc = (By.XPATH, "//button[@data-bind='click:$root.addImage']")
    host_loc = (By.XPATH, "//button[@data-bind='click: $root.addHost']")
    storage_pool_loc = (By.XPATH, '//button[@data-bind="click:$root.addStoragePool"]')
    cpu_loc = (By.ID, 'resource_instance_cpu')
    memory_loc = (By.ID, 'resource_instance_memory')
    sysdisk_loc = (By.ID, "storage_input_id")
    ip_pool_loc = (By.ID, 'create_vm_ip_pool_id')

    # 服务选择页面
    service_search_input_loc = (By.XPATH, "//span[text()='服务名称']/../input")         # 服务搜索输入框
    service_confirm_loc = (By.XPATH, "//button[text()='确定']")                 # 确定按钮

    # VDC选择页面
    vdc_search_input_loc = (By.XPATH, "//span[text()='VDC名称']/../input")
    vdc_confirm_loc = (By.XPATH, "//button[text()='确认' and @data-bind='click: vdcSave']")

    # 归属用户选择页面
    user_search_input_loc = (By.XPATH, "//span[text()='账号']/../input")
    user_confirm_loc = (By.XPATH, "//button[text()='确认' and @data-bind='click: saveUsers']")

    # 业务系统选择页面
    bussys_search_input_loc = (By.XPATH, "//span[text()='业务系统名称']/../input")
    bussys_confirm_loc = (By.XPATH, "//button[text()='确认' and @data-bind='click: busSysSave']")

    # 应用集群选择页面
    busitem_search_input_loc = (By.XPATH, "//span[text()='应用集群名称']/../input")
    busitem_confirm_loc = (By.XPATH, "//button[text()='确认' and @data-bind='click: busItemSave']")

    # 镜像选择页面
    image_search_input_loc = (By.XPATH, "//span[text()='镜像名称']/../input")
    image_confirm_loc = (By.XPATH, "//button[text()='确认' and @data-bind='click: imageSave']")

    # 宿主机选择页面(通过IP)
    host_search_input_loc = (By.XPATH, "//span[text()='IP地址']/../input")
    host_confirm_loc = (By.XPATH, "//button[text()='确认' and @data-bind='click:hostSave']")

    # 存储池选择页面
    storage_pool_search_input_loc = (By.XPATH, "//span[text()='存储池名称']/../input")
    storage_pool_confirm_loc = (By.XPATH, "//button[text()='确认' and @data-bind='click:storagePoolSave']")

    def enter_menu(self):
        '''
        进入云主机创建页面
        '''
        self.click_element(*self.virtual_recourse_manage_loc)
        self.click_element(*self.recourse_instance_loc)
        self.click_element(*self.create_button_lov)
        self.vclog.info('进入云主机创建页面')


    def search_for(self, item_type, item_value):
        '''
        用于需要通过弹出窗口进行选择的控件,根据item_type和item_value调用不同的组件进行搜索
        :Args:
         - item_type: 组件类型
         - item_value: 组件值

        '''
        self.vclog.info(f'{item_type}：{item_value}')
        if item_type == '归属服务':
            self.click_element(*self.service_loc)
            self.set_value(item_value, *self.service_search_input_loc)
        elif item_type == '归属VDC':
            self.click_element(*self.vdc_loc)
            self.set_value(item_value, *self.vdc_search_input_loc)
        elif item_type == '归属用户':
            self.click_element(*self.user_loc)
            self.set_value(item_value, *self.user_search_input_loc)
        elif item_type == '业务系统':
            if item_value:             # 非必填，有传值才进行操作
                self.click_element(*self.bussys_loc)
                self.set_value(item_value, *self.bussys_search_input_loc)
            else:
                return True
        elif item_type == '应用集群':
            if item_value:             # 非必填，有传值才进行操作
                self.click_element(*self.busitem_loc)
                self.set_value(item_value, *self.busitem_search_input_loc)
            else:
                return True
        elif item_type == '镜像':
            self.click_element(*self.image_loc)
            self.set_value(item_value, *self.image_search_input_loc)
        elif item_type == '宿主机':
            self.click_element(*self.host_loc)
            self.set_value(item_value, *self.host_search_input_loc)
        elif item_type == '存储池':
            self.click_element(*self.storage_pool_loc)
            self.set_value(item_value, *self.storage_pool_search_input_loc)
        self.vclog.info('点击搜索按钮')
        self.click_element(*self.search_button_loc)         # 点击搜索按钮
        self.vclog.info('勾选第一个搜索结果')
        try:
            self.click_element(*self.first_search_result_loc)    # 勾选第一个搜索结果
        except Exception as err:
            self.vclog.warning(f'搜索不到对应结果:{err}')
            raise Exception


    def item_click(self, item_type, item_value):
        '''
        搜索之后点击确认

        :Args:
         - item_type: 组件类型
         - item_value: 组件值

        '''
        self.search_for(item_type, item_value)
        if item_type == '归属服务':
            self.click_element(*self.service_confirm_loc)
        elif item_type == '归属VDC':
            self.click_element(*self.vdc_confirm_loc)
        elif item_type == '归属用户':
            self.click_element(*self.user_confirm_loc)
        elif item_type == '业务系统':
            if item_value:
                self.click_element(*self.bussys_confirm_loc)
        elif item_type == '应用集群':
            if item_value:
                self.click_element(*self.busitem_confirm_loc)
        elif item_type == '镜像':
            self.click_element(*self.image_confirm_loc)
        elif item_type == '宿主机':
            self.click_element(*self.host_confirm_loc)
        elif item_type == '存储池':
            self.click_element(*self.storage_pool_confirm_loc)


    def item_select(self, item_type, item_value):
        '''
        下拉列表的处理
        :Args:
         - item_type: 组件类型
         - item_value: 组件值

        '''
        if item_type == '到期时间':
            self.select_by_text(item_value, *self.applytime_timefor_loc)
        elif item_type == '可用分区':
            self.select_by_text(item_value, *self.az_loc)
        elif item_type == 'CPU':
            self.select_by_text(item_value, *self.cpu_loc)
        elif item_type == '内存':
            self.select_by_text(item_value, *self.memory_loc)
        elif item_type == 'IP池':
            self.select_by_text(item_value, *self.ip_pool_loc)
        self.vclog.info(f'下拉{item_type}，选择{item_value}')


    def input_item(self, item_type, item_value):
        '''
        根据输入的类型和值进行填充
        :Args:
         - item_type: 组件类型
         - item_value: 组件值

        '''
        self.vclog.info(f'{item_type}：{item_value}')
        if item_type == '云主机名称':
            self.set_value(item_value, *self.name_input_loc)
        elif item_type == 'VM Name':
            self.set_value(item_value, *self.vmname_input_loc)
        elif item_type == 'Hostname':
            self.set_value(item_value, *self.hostname_input_loc)
        elif item_type == '备注':
            self.set_value(item_value, *self.textarea_input_loc)
        elif item_type == '系统盘':
            if item_value:  # 有值才重新赋值
                self.set_value(item_value, *self.sysdisk_loc)
        elif item_type == '到期时间':
            if item_value == '永久':
                self.click_element(*self.applytime_datefor_loc)
            elif '年' in item_value or '月' in item_value:
                self.click_element(*self.applytime_time_loc)
                self.item_select(item_type, item_value)
            else:
                self.click_element(*self.applytime_date_loc)
                self.set_value(item_value, *self.applytime_datefor_loc)
                self.click_element(*self.textarea_input_loc)      # 用于取消日历控件
        elif item_type in ['可用分区', 'CPU', '内存', 'IP池']:     # 需要下拉选择的控件
            self.item_select(item_type, item_value)
        else:       # 需要搜索的控件
            self.item_click(item_type, item_value)
