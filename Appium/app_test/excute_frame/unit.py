import unittest
from Appium.app_test.excute_frame.app_start import app_start
import logging
from time import sleep

# 定义前后置条件为：打开APP和关闭APP
class condition(unittest.TestCase):

    def setUp(self):
        logging.info('======开始setUp=========')
        self.driver = app_start()

    def tearDown(self):
        logging.info('======结束tearDown=====')
        sleep(5)
        self.driver.close_app()
