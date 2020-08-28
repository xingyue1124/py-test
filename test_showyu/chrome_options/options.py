from selenium import webdriver


# 创建一个Options类
class Options:
    def conf_option(self):
        # 创建chromeoptions对象
        options = webdriver.ChromeOptions()

        # 浏览器启动，窗体最大化
        options.add_argument('start-maximized')
        # 无头模式（可选择性开启）
        options.add_argument('--headless')
        # 去掉启动浏览器后的开发者警告
        options.add_experimental_option('useAutomationExtension', False)
        # 去掉黄条（启动浏览器后的提示：浏览器正在收自动化工具控制...)
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 去掉密码管理弹窗（登录后提示是否保存账密的弹窗）
        prefs = {"": ""}
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        options.add_experimental_option("prefs", prefs)
        return options
