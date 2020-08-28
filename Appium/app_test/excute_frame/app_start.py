import yaml
import logging.config
from appium import webdriver

# 读取日志配置文件
CON_LOG = '../runlog/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def app_start():
    # 读取参数yaml文件
    stream = open('../yaml/parameter.yaml', 'r')
    data = yaml.load(stream, Loader=yaml.FullLoader)

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
    # 配置键盘，如果需要输入中文，需配置
    parameter['unicodeKeyboard'] = data['unicodeKeyboard']
    parameter['resetKeyboard'] = data['resetKeyboard']
    stream.close()

    logging.info('开始跑app...')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', parameter)

    driver.implicitly_wait(10)
    return driver


if __name__ == '__main__':
    app_start()
