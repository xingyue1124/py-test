from Appium.app_test.excute_frame.base_class import base_class
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
from Appium.app_test.excute_frame.app_start import app_start


class public(base_class):
    # 定位取消和跳过按钮
    cancel = (By.ID, 'android:id/button2')
    skip = (By.ID, 'com.tal.kaoyan:id/tv_skip')

    def check_cancel(self):
        logging.info("============开始检查取消按钮===============")

        try:
            cancel = self.driver.find_element(*self.cancel)
        except NoSuchElementException:
            logging.info('取消按钮没有找到')
        else:
            logging.info('点击取消')
            cancel.click()

    def check_skip(self):
        logging.info("==========开始检查跳过按钮===========")
        try:
            skip = self.driver.find_element(*self.skip)
        except NoSuchElementException:
            logging.info('跳过按钮没有找到')
        else:
            logging.info('点击跳过')
            skip.click()


if __name__ == '__main__':
    driver = app_start()
    com = public(driver)
    com.check_cancel()
    com.check_skip()
