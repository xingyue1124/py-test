from appium import webdriver
import yaml

# 读取参数yaml文件
file = open('parameter.yaml', 'r')
data = yaml.load(file, Loader=yaml.FullLoader)

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

# 建立连接
driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', parameter)
