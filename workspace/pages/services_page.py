# coding=utf-8
'''
    Created on 2018-10-09
    @author: wjx
    Project:服务管理页面
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from workspace.pages.base_page import BasePage

class ServicesPage(BasePage):
    """
    服务管理页面
    """
    breadcrumb_loc = (By.XPATH, "//ul[@class='breadcrumb']//li[@class='active']")   # 面包屑地址
    addDir_loc = (By.XPATH, "//div[@class='widget-buttons']/span[1]")               # 服务目录创建按钮
    delDir_loc = (By.XPATH, "//div[@class='widget-buttons']/span[2]")               # 服务目录删除按钮
    editDir_loc = (By.XPATH, "//div[@class='widget-buttons']/span[3]")              # 服务目录编辑按钮
    serviceDir_loc = (By.XPATH, "//label[@class='widget-caption']/strong")          # 服务目录标题
    serviceType_loc = (By.XPATH, "//span[@class='widget-caption']/span")            # 服务类型
    serviceCreate_loc = (By.XPATH, "//a[text()='创建服务 ']")                        # 创建服务按钮
    serviceStatus_loc = (By.XPATH, "//span[text()='服务状态']/../select")            # 服务状态下拉框
    serviceSearch_loc = (By.XPATH, "//span[text()='服务名称']/../input")             # 服务名称搜索框
    searchbutton_loc = (By.XPATH, "//button[text()='搜索']")                         # 搜索按钮
    resetbutton_loc = (By.XPATH, "//button[text()='重置']")                          # 重置按钮
    


