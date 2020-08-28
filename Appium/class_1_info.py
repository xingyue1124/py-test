from appium import webdriver

# 定义一个字典去存储信息
info = {}
# 操作系统
info['platformName'] = 'Android'
# 模拟器
# 操作系统版本
info['platformVersion'] = '5.1.1'
# 模拟器类型
info['deviceName'] = '127.0.0.1:62001'  # 真机需要设备名或型号
# 真机udid
# info['udid'] = '手机USB连接的串码'  # 连接手机后，可通过adb devices查看
# app路径
info['app'] = r'C:\Users\xingy\Desktop\kaoyan3.1.0.apk'
# app包名
info['appPackage'] = 'com.tal.kaoyan'
info['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'
# 重置应用状态
info['noReset']='False'
# 配置键盘，如果需要输入中文，需配置
info['unicodeKeyboard']='True'
info['resetKeyboard']='True'
# 如果需要获取APP的toast提示，需配置
info['automationName']='uiautomator2'

# 建立连接
driver = webdriver.Remote('http://localhost:4723/wd/hub',info)
# 设置隐式等待
driver.implicitly_wait(10)