import pytest

def test_01():
    print('111111')

def test_02():
    print('222222')

@pytest.mark.skipif(4>3,reason="reason")
def test_03():
    print('333333')

class Testaa():
    def test_04(self):
        print('444444')

if __name__ == '__main__':
    # 以列表形式存放多个参数
    pytest.main(["-s","test_pytest1.py"])