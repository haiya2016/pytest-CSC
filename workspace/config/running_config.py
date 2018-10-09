"""
用例运行时的一些配置，例如调用哪个浏览器
"""
from selenium import webdriver

def get_driver(driver_type='chrome'):
    '''
    返回一个浏览器，默认为chrome，否则为IE
    '''
    if driver_type == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Ie()
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(60)
    driver.set_window_size(1366, 768)
    return driver
    