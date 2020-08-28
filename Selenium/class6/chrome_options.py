from selenium import webdriver

class Options:
    def options_conf(self):

        # 创建chromeOptions对象
        options = webdriver.ChromeOptions()
        # 窗体最大化
        options.add_argument('start-maximized')

        # 无头模式： 启动浏览器进程，但是不会显示出来
        # options.add_argument('--headless')

        # 去掉开发者警告
        options.add_experimental_option('useAutomationExtension', False)
        # 去掉黄条
        options.add_experimental_option('excludeSwitches', ['enable-automation'])

        # 去掉密码管理弹窗
        prefs = {'':''}
        prefs['credentials_enable_service'] = False
        prefs['profile.password_manager_enabled'] = False
        options.add_experimental_option('prefs',prefs)

        return options



