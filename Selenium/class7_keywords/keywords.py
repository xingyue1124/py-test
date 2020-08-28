# 基于WebUI实现的自动化，所以调用selenium模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from Selenium.class6.chrome_options import Options
from time import sleep
from Selenium.class7_log.log import Logger

'''
    设计WebUI的关键字驱动类对象：
    对常用的关键字进行二次封装，以便于后续的调用
'''


# 创建浏览器对象 v1.0：必须判断，不然其他人不清楚。
def open_browser1(browser_type):
    if browser_type is 'Chrome':
        driver = webdriver.Chrome()
    elif browser_type is 'Firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    return driver


# 创建浏览器对象 v2.0：通过反射机制实现
def open_browser(browser_type):
    # 添加异常处理机制，确保健壮性
    try:
        if browser_type == 'Chrome':
            Logger().get_logger().info('Chrome浏览器正在启动中......')
            driver = webdriver.Chrome(options=Options().options_conf())
        else:
            Logger().get_logger().info('{0}浏览器正在启动中......'.format(browser_type))
            driver = getattr(webdriver, browser_type)()
    except Exception as e:
        Logger().get_logger().info('出现异常，默认调用Chrome浏览器，异常信息：\n{0}'.format(e))
        driver = webdriver.Chrome()
    return driver


class WebUIKeys:
    # 构造函数
    def __init__(self, browser_type):
        self.driver = open_browser(browser_type)

    # 元素定位 v1.0：八种元素定位
    def locator1(self, loc_type, value):
        if loc_type is 'xpath':
            return self.driver.find_element_by_xpath(value)
        elif loc_type is 'id':
            return self.driver.find_element_by_id(value)

    # 元素定位 v2.0：基于元组形式来实现元素定位。ex：(By.ID,'kw')
    # 传入的By对象要确保是对象，而非str类型
    def locator2(self, loc):
        # 错误例子
        # demo = "ID"
        # loc_type = "By." + demo  # 这里是str而非object
        # value = "kw"
        return self.driver.find_element(*loc)

    # 元素定位 v3.0：基于字符串来实现元素定位，调用Python反射机制
    def locator(self, name, value, *arg):
        # 反射机制中，有一个函数叫做getattr()
        # upper()将字符串转为大写格式
        # getattr(By,name.upper()):传入name.upper()为ID则调用By对象中的属性By.ID
        # name='id'，value='kw'
        # self.driver.find_element(By.ID, 'kw')
        try:
            return self.driver.find_element(getattr(By, name.upper()), value)
        except Exception as e:
            pass

    # 元素的输入操作
    def input(self, name, value, txt):
        self.locator(name, value).send_keys(txt)

    # 元素的点击操作
    def click(self, name, value):
        self.locator(name, value).click()

    # 浏览器关闭
    def quit(self):
        self.driver.quit()

    # 访问指定URL
    def visit(self, url):
        self.driver.get(url)

    # 强制等待
    def sleep(self, time):
        sleep(time)

    # 隐式等待
    def wait(self, time):
        self.driver.implicitly_wait(time)

    # 获取文本
    def get_title(self):
        return self.driver.title

    # 断言机制：获取元素的文本信息，进行比对校验
    def assert_text(self, function_name, value, expect):
        reality = self.locator(function_name, value).text
        try:
            assert reality == expect
            Logger().get_logger().info('断言成功，流程正确！')
            return True
        except Exception as e:
            Logger().get_logger().info('出现异常，异常信息：\n{0}'.format(e))
            return False