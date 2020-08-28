# import unittest,os
# from selenium import webdriver
# from BeautifulReport import BeautifulReport
# import time
#
# class UnitDemo(unittest.TestCase):
#
#     def save_img(self,test_method):  # 失败截图方法（必须要定义在class中）
#         root_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\','/')
#         # root_dir = C:\Users\xingy\PycharmProjects\untitled\Selenium\class_10
#         img_path = root_dir + '/img'
#         # img_path = C:\Users\xingy\PycharmProjects\untitled\Selenium\class_10\img
#         self.driver.get_screenshot_as_file('{}/{}.png'.format(img_path,test_method))
#
#     def setUp(self) -> None:
#         self.driver = webdriver.Chrome()
#
#     def tearDown(self) -> None:
#         self.driver.quit()
#
#     # 想要在失败后有报错截图的产生
#     @BeautifulReport.add_test_img('test_1')
#     def test_1(self):
#         driver = webdriver.Chrome()
#         driver.get('http://www.baidu.com')
#         driver.find_element_by_id('kw111').send_keys('123456')
#         self.driver.find_element_by_id('su').click()
#         time.sleep(5)



import unittest, time,os
from selenium import webdriver
from BeautifulReport import BeautifulReport

class test_remote(unittest.TestCase):
    def save_img(self, test_method): # 失败截图方法（必须要定义在class中）
        root_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\','/')
        img_path = root_dir + '/img'
        self.driver.get_screenshot_as_file('{}/{}.png'.format(img_path, test_method))

    def setUp(self):
        self.driver = webdriver.Chrome()

    @BeautifulReport.stop # 不执行该用例
    def test_zhaolei(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('赵雷')
        self.driver.find_element_by_id('su').click()
        time.sleep(5)

    @BeautifulReport.add_test_img('test_zhoujielun')# 失败后会有报错截图
    def test_zhoujielun(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_id('kwk').send_keys('周杰伦')# 这里的id我故意写错来查看效果
        self.driver.find_element_by_id('su').click()
        time.sleep(5)

    def test_ig(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('IG')
        self.driver.find_element_by_id('su').click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()