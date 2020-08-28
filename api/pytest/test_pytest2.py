import pytest

def setup_module():
    print('模块级别的setup')
def teardown_module():
    print('模块级别的teardown')

def test_01():
    print('111111')

def test_02():
    print('222222')

def test_03():
    print('333333')

class Testaa():
    def test_04(self):
        print('444444')
    def test_05(self):
        print('555555')

if __name__ == '__main__':
    # 以列表形式存放多个参数
    pytest.main(["-s","test_pytest2.py"])