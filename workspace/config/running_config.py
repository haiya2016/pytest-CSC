"""
用例运行时的一些配置，例如调用哪个浏览器
"""
from selenium import webdriver

def chrome_driver():
    '''
    返回一个chrome浏览器
    '''
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(60)
    driver.set_window_size(1366, 768)
    return driver