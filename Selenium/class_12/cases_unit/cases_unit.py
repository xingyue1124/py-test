import unittest
from selenium import webdriver
from time import sleep
from Selenium.class_12.page_object.login_page import LoginPage
from Selenium.class_12.page_object.info_page import InforPage


class CasesUnit(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        sleep(5)
        self.driver.quit()

    '''
        UnitTest中先运行setup，再执行case，再执行tearDown
        如果PO对象有关联，就通过driver进行关联
        1. driver在loginPage，执行了登录的操作，记录下登录状态
        2. 将这个driver传到第二个页面，执行登录后才能执行的操作
    '''

    # 用例流程
    def test_1(self):
        # 页面对象在实例化的时候都需要传递一个driver，不同的driver会执行不同的操作
        lp = LoginPage(self.driver, LoginPage.url)
        lp.test_login('666666', '111111')
        ip = InforPage(self.driver, InforPage.url)
        ip.test_infor('虚竹')


if __name__ == '__main__':
    unittest.main()