# 应用UnitTest框架
import unittest
from Selenium.class7_keywords.keywords import WebUIKeys
from time import sleep


# 调用UnitTest框架
class UnitDemo(unittest.TestCase):
    # 前置条件，有且只有一个，类级别，类调用时才会运行一次
    @classmethod
    def setUpClass(cls) -> None:
        print('this is class setup')
        # cls.wk = WebUIKeys('Chrome')

    # 前置条件，有且只有一个，用例版本
    def setUp(self) -> None:
        self.wk = WebUIKeys('Chrome')
        self.wk.wait('arg', 'arg1', 10)
        # pass

    # 后置条件，有且只有一个，用例版本
    def tearDown(self) -> None:
        self.wk.quit()

    # 后置条件，类级别
    @classmethod
    def tearDownClass(cls) -> None:
        print('this is class teardown')

    # 创建测试用例：依照框架规则，需要以test_命名
    # 用例流程一：百度搜索
    def test_case0(self):
        self.wk.visit(1, 2, 'http://www.baidu.com')
        title = self.wk.get_title()
        self.assertEqual(first='123', second=title, msg='123123123')

    # 用例流程二：登录页面
    # def test_case1(self):
    #     self.wk.visit(1, 2, 'http://39.98.138.157/shopxo/index.php')
    #     self.wk.click('xpath', '//a[text()="登录"]')

    # 普通函数
    def normal(self):
        print('function')


if __name__ == '__main__':
    # unittest框架运行的方式1
    unittest.main()
