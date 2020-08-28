from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 定义基类：提供各个PO对象来调用的公共类方法
class BasePage(object):
    # 定义构造函数：所有内容都是基于driver操作，所以要传递driver
    # 定义构造函数：每一个页面都有url，定义好url，在类中直接可以调用
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    # 元素的定位
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 访问指定的URL
    def visit(self):
        self.driver.get(self.url)

    # 关闭浏览器
    def quit(self):
        sleep(3)
        self.driver.quit()