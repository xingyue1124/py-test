import pytest

# 定义fixture的级别为class
@pytest.fixture(scope="class")
def fixturemethod():
    b = "bbb"
    print("bbbbbbbbbbbbbbbbbbbbbbb")
    return b


def test_01(fixturemethod):
    name = "bbb"
    print("找到01的fixturemethod")
    assert fixturemethod == name


def test_02(fixturemethod):
    name = "bbb"
    print("找到02的fixturemethod")
    assert fixturemethod == name


class Testaa:

    def test_04(self, fixturemethod):
        name = "bbb"
        print("找到04的fixturemethod")
        assert fixturemethod == name

    def test_05(self, fixturemethod):
        name = "bbb"
        print("找到05的fixturemethod")
        assert fixturemethod == name


if __name__ == '__main__':
    pytest.main(['-s', 'test_scope.py'])
