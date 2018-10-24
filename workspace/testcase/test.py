from selenium import webdriver

dr1 = webdriver.Chrome()
dr2 = webdriver.Chrome()

dr1.get('http://www.baidu.com')
dr2.get('http://www.sina.com')