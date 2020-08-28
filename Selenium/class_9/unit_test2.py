# 应用UnitTest框架
import unittest
from Selenium.class7_keywords.keywords import WebUIKeys
from time import sleep

# 调用UnitTest框架
class UnitDemo(unittest.TestCase):

    # 前置条件，有且只有一个，用例版本
    def setUp(self) -> None:
        self.wk = WebUIKeys('Chrome')
        self.wk.wait(10)

    # 后置条件，有且只有一个，用例版本
    def tearDown(self) -> None:
        self.wk.quit()


    # 创建测试用例：依照框架规则，需要以test_开头命名
    # 百度搜索
    def test_case01(self):
        self.wk.visit('http://www.baidu.com')
        self.wk.input('id','kw','软件测试')
        self.wk.click('id','su')
        # 加入断言
        title = self.wk.get_title()
        self.assertEqual(title,'百度一下，你就知道', msg='断言失败')
        sleep(3)

    @unittest.skip   # 无条件跳过执行
    # 登录页面
    def test_case02(self):
        self.wk.visit('http://39.98.138.157/shopxo/index.php')
        self.wk.click('xpath', '//a[text()="登录"]')
        self.wk.input('name','accounts', '666666')
        self.wk.input('name', 'pwd', '111111')
        self.wk.click('xpath', '/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button')
        sleep(2)

    @unittest.skipUnless(1==2, '1==1条件')    # 条件为真时，执行该用例；反之，不执行（跳过）
    def test_case03(self):
        print("this is case03!")

    @unittest.skipIf(1==1, '1==2条件')   # 条件为假时，执行该用例；反之，不执行（跳过）
    def test_case04(self):
        print("this is case04!")

    @unittest.expectedFailure    # 当用例报错，系统选择忽略
    def test_case05(self):
        self.assertEqual('a', 'b', msg='not equal')

if __name__ == '__main__':
    # unittest框架运行的方式1：
    unittest.main()


