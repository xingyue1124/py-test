from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

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
driver.implicitly_wait(30)


# 启动APP后检查是否有提示更新弹窗的“取消”按钮和引导页面的“跳过”按钮
def check_cancel():
    print("开始检查是否有取消")

    try:
        cancel = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        print('没有取消按钮')
    else:
        cancel.click()


def check_skip():
    print("开始检查是否有跳过")
    try:
        skip = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        print("没有跳过")
    else:
        skip.click()

#最后去调用这两个方法
check_cancel()
check_skip()