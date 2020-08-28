from selenium import webdriver
from time import sleep

# 创建chromeOptions对象
options = webdriver.ChromeOptions()
# 窗体最大化
options.add_argument('start-maximized')

# 无头模式： 启动浏览器进程，但是不会显示出来
# options.add_argument('--headless')

# 启动隐身模式
# options.add_argument('incognito')

# 读取本地缓存，这个操作非常不推荐使用
# options.add_argument(r'--user-data-dir=C:\Users\xingy\AppData\Local\Google\Chrome\User Data')

# 去掉开发者警告
options.add_experimental_option('useAutomationExtension', False)
# 去掉黄条
options.add_experimental_option('excludeSwitches', ['enable-automation'])

# 去掉密码管理弹窗
prefs = {'':''}
prefs['credentials_enable_service'] = False
prefs['profile.password_manager_enabled'] = False
options.add_experimental_option('prefs',prefs)


# 创建chrome对象
# driver = webdriver.Chrome(options=options)
# driver.implicitly_wait(10)
# driver.get('http://www.baidu.com')
# driver.find_element_by_id('kw').send_keys('测码学院')
# driver.find_element_by_id('su').click()
# sleep(2)
# print(driver.title)
# driver.quit()

