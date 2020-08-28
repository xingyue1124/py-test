import pytest


def test_allure():
    print("this is allure test")
    assert 1 == 1


if __name__ == '__main__':
    pytest.main(['-s', '--alluredir', './report/xml'])
