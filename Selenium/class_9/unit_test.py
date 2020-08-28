# 应用UnitTest框架
import unittest

# 调用UnitTest框架
class UnitDemo(unittest.TestCase):

    # 前置条件，有且只有一个，类级别，类调用时才会运行一次
    @classmethod
    def setUpClass(cls) -> None:
        print('this is class setup')

    # 前置条件，有且只有一个，用例版本
    def setUp(self) -> None:
        print('this is setup')

    # 后置条件，有且只有一个，用例版本
    def tearDown(self) -> None:
        print('this is teardown')

    # 后置条件，类级别
    @classmethod
    def tearDownClass(cls) -> None:
        print('this is class teardown')


    # 创建测试用例：依照框架规则，需要以test_开头命名
    def test_case01(self):
        print('this is case01!')

    def test_case02(self):
        print('this is case02!')


if __name__ == '__main__':
    # unittest框架运行的方式1：
    unittest.main()


