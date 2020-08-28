import logging
from Appium.app_test.kaoyan_excute.public_class import public
from Appium.app_test.excute_frame.app_start import app_start
from selenium.webdriver.common.by import By


class login(public):
    # 定位用户名、密码及登录按钮
    username_type = (By.ID, 'com.tal.kaoyan:id/login_email_edittext')
    pwd_type = (By.ID, 'com.tal.kaoyan:id/login_password_edittext')
    login_button = (By.ID, 'com.tal.kaoyan:id/login_login_btn')

    # 开始登录
    def login_begin(self, username, pwd):
        self.check_cancel()
        self.check_skip()

        logging.info('===============登录===============')
        logging.info('输入用户名:%s' % username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info('输入密码:%s' % pwd)
        self.driver.find_element(*self.pwd_type).send_keys(pwd)

        logging.info('点击登录按钮.')
        self.driver.find_element(*self.login_button).click()
        logging.info('登录完成 ')


if __name__ == '__main__':
    driver = app_start()
    l = login(driver)
    l.login_begin('beryl1124', 'xy123456')
