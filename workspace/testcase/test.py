# coding:utf-8
from selenium import webdriver

browser = webdriver.Chrome()
# 设置页面等待时间
browser.implicitly_wait(10)

browser.get("https://mail.163.com/")
#  切换到iframe
iframe = browser.find_element_by_xpath('//*[@id="loginDiv"]//iframe')
browser.switch_to.frame(iframe)

username='rachellan168'
browser.find_element_by_name("email").send_keys(username)
passwd='198512265201314'
browser.find_element_by_name("password").send_keys(passwd)
browser.find_element_by_id("dologin").click()

