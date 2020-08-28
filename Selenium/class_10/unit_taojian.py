# 应用UnitTest框架
import unittest


# 调用UnitTest框架
class UnitDemo(unittest.TestCase):

    # 前置条件，有且只有一个，用例版本
    def setUp(self) -> None:
        print("setup")

    # 后置条件，有且只有一个，用例版本
    def tearDown(self) -> None:
        print("teardown")

    # 创建测试用例：依照框架规则，需要以test_开头命名
    def test_case01(self):
        print("this is case01!")


    def test_case02(self):
        print("this is case02!")


    def test_case03(self):
        print("this is case03!")


    def test_case04(self):
        print("this is case04!")


    def test_case05(self):
        print("this is case05!")

if __name__ == '__main__':
    # unittest框架运行的方式1：
    unittest.main()


