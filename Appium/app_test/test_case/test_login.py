from Appium.app_test.excute_frame.unit import condition
from Appium.app_test.kaoyan_excute.login import login
import unittest
import logging

# 使用unittest来管理用例
class Test_login(condition):

    def test_login_cm01(self):
        logging.info('=========开始登录01==========')
        l = login(self.driver)
        l.login_begin('beryl1124', 'xy123456')

    # def test_login_cm02(self):
    #     logging.info('==========开始登录02=========')
    #     l = login(self.driver)
    #     l.login_begin('111', '222')
    #
    # def test_login_error(self):
    #     logging.info('=========开始登录03==========')
    #     l = login(self.driver)
    #     l.login_begin('666', '888')


if __name__ == '__main__':
    unittest.main()
