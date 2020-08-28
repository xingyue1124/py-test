# 导包
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_showyu.chrome_options.options import Options
from test_showyu.log.log import Logger


# 浏览器运行初始化
def open_browser(browser_type):
    try:
        if browser_type == 'Chrome':
            Logger().get_logger().info('Chrome浏览器启动中......')
            driver = webdriver.Chrome(options=Options().conf_option())
        else:
            Logger().get_logger().info('{0}浏览器启动中......'.format(browser_type))
            # 使用反射机制启动对应浏览器
            driver = getattr(webdriver, browser_type)()
    except Exception as e:
        Logger().get_logger().info('出现异常，启动Chrome浏览器，Exception信息：{0}'.format(e))
        # 启动失败，默认自动Chrome浏览器
        driver = webdriver.Chrome()
    return driver


class WebUI_Framework():
    # 创建日志对象
    log = Logger().get_logger()

    # 初始化
    def __init__(self, browser_type):
        self.driver = open_browser(browser_type)

    # 访问指定的URL
    def visit(self, **kwargs):
        self.driver.get(kwargs['txt'])

    # 定位元素
    def locator(self, **kwargs):
        try:
            # 利用反射机制从By中获取类属性
            return self.driver.find_element(getattr(By, kwargs['loc'].upper()), kwargs['value'])
        except Exception as e:
            print('元素定位失败，信息：{0}'.format(e))

    # 进行点击操作
    def click(self, **kwargs):
        self.locator(**kwargs).click()

    # 进行输入操作
    def input(self, **kwargs):
        self.locator(**kwargs).send_keys(kwargs['txt'])

    # 进行清空操作
    def clear(self, **kwargs):
        self.locator(**kwargs).clear()

    # 强制等待
    def sleep(self, **kwargs):
        time.sleep(kwargs['txt'])

    # 隐式等待
    def wait(self, **kwargs):
        self.driver.implicitly_wait(kwargs['txt'])

    # 切换至新窗体
    def switch_to_new_current(self, **kwargs):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])

    # 关闭旧窗体
    def close_old_current(self, **kwargs):
        self.driver.close()

    # 切换至旧窗体
    def switch_to_old_current(self, **kwargs):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])

    # 切换至新窗体，并关闭旧窗体
    def switch_and_close(self, **kwargs):
        handles = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to.window(handles[1])

    # 切换至Iframe窗体
    def switch_to_iframe(self, **kwargs):
        self.driver.switch_to.frame(self.locator(**kwargs))

    # 切换回默认窗体
    def switch_to_default(self, **kwargs):
        self.driver.switch_to.default_content()

    # 关闭浏览器
    def quit(self, **kwargs):
        self.driver.quit()

    # 文本断言
    def assert_text(self, **kwargs):
        reality = self.locator(**kwargs).text
        try:
            assert reality == kwargs['expect']
            return True
        except:
            Logger().get_logger().info('断言失败,断言信息：{0} != {1}'.format(reality, kwargs['expect']))
            return False
