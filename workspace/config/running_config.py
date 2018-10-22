"""
用例运行时的一些配置，例如调用哪个浏览器、保存cookie文件
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

def save_cookie(driver):
    '''
    保存cookie到文件，路径为'.\\workspace\\data\\cookie.txt'
    '''
    cookie_items = driver.get_cookies()
    cookies = {}   # 定义一个空的字典，存放cookies内容
    # 获取到的cookies是列表形式，将cookies转成json形式并存入本地名为cookie的文本中
    for cookie_item in cookie_items:
        cookies[cookie_item['name']] = cookie_item['value']
    with open('.\\workspace\\data\\cookie.txt', 'w+', encoding='utf-8') as cookie_file:
        cookie_file.write(cookies)
