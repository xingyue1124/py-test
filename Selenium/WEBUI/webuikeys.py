from selenium import webdriver
from Selenium.WEBUI.log import Logger
from Selenium.class6.chrome_options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

class WebUiKeys:
    #定义构造函数
    def __init__(self, browse_type):
        #获取日志器
        self.logger = Logger().get_logger()
        #启动浏览器
        self.driver = self.open_browse(browse_type)

    # 启动浏览器
    def open_browse(self, browse_type):
        try:
            self.logger.info('{0}浏览器正在启动中....'.format(browse_type))
            if browse_type == 'Chrome':
                # 配置Chrome浏览器选项
                options = Options().options_conf()
                # 启动Chrome浏览器
                driver = webdriver.Chrome(options=options)
            else :
                # 根据浏览器类型启动不同浏览器
                driver = getattr(webdriver, browse_type)()
        except Exception as error:
            self.logger.info('出现异常，默认调用Chrome浏览器，异常信息：\n{0}'.format(error))
            # 启动浏览失败，默认启动Chrome浏览器
            driver = webdriver.Chrome()
        return driver

    #访问指定的Url
    def get_url(self, **kwargs):
        self.driver.get(kwargs['text'])

    #定位元素
    def locator(self, **kwargs):
        #利用反射机制从By中获取类属性
        return  self.driver.find_element(getattr(By, kwargs['type'].upper()), kwargs['value'])

    #进行输入操作
    def input(self, **kwargs):
        self.locator(**kwargs).send_keys(kwargs['text'])

    #进行点击操作
    def click(self, **kwargs):
        self.locator(**kwargs).click()

    #强制等待
    def sleep(self, **kwargs):
        sleep(kwargs['text'])

    #隐式等待
    def wait(self, **kwargs):
        print(kwargs['text'])
        self.driver.implicitly_wait(kwargs['text'])

    #显示等待定位元素
    def eleWait(self, **kwargs):
        wait = WebDriverWait(self.driver, kwargs['text'], 0.5)
        return wait.until(lambda el : self.locator(**kwargs), message="元素定位失败")

    #断言，判断实际结果是否与预期一致
    def assert_text(self, **kwargs):
        #显示等待定位元素
        el = self.eleWait(**kwargs)
        reality = el.text
        try:
            print(reality, kwargs['expect'])
            assert reality == kwargs['expect']
            Logger().get_logger().info("断言成功，流程正确！")
            return True
        except Exception as error :
            self.logger.info("出现异常：{0}".format(error))
            return False

    #关闭浏览器当前标签页
    def close(self):
        self.driver.close()

    #关闭浏览器，释放浏览器
    def quit(self):
        self.driver.quit()

    #不定长参数
    def getParamters(self, *args):
        list=[]
        for x in args:
            if x is None:
                pass
            else :
                list.append(x)
        return list