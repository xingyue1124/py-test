from appium import webdriver
import yaml
from selenium.common.exceptions import NoSuchElementException
# 导入日志模块
import logging
import logging.config

stream = open('../yaml/parameter.yaml', 'r')
data = yaml.load(stream, Loader=yaml.FullLoader)

# 读取日志配置文件
CON_LOG = '../runlog/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


# 声明配置信息
parameter = {}
# 系统信息
parameter['platformName'] = data['platformName']
# 版本信息
parameter['platformVersion'] = data['platformVersion']
# 设备名称
parameter['deviceName'] = data['deviceName']
parameter['app'] = data['app']
# 是否重置
parameter['noReset'] = data['noReset']
# 包名和启动页参数
parameter['appPackage'] = data['appPackage']
parameter['appActivity'] = data['appActivity']

logging.info('start app...')
driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', parameter)


# 启动APP后检查是否有提示更新弹窗的“取消”按钮和引导页面的“跳过”按钮
def check_cancel():
    logging.info("开始检查是否有取消")

    try:
        cancel = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        logging.info('没有取消按钮')
    else:
        cancel.click()


def check_skip():
    logging.info("开始检查是否有跳过")
    try:
        skip = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        logging.info("没有跳过")
    else:
        skip.click()


# 最后去调用这两个方法
check_cancel()
check_skip()

# 设置隐式等待
driver.implicitly_wait(15)