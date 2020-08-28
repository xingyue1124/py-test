import pytest

@pytest.fixture()
def start():
    print("========开始========")

# 通过标记调用声明的fixture函数
@pytest.mark.usefixtures("start")
def test_a():
    print("=======执行a========")

if __name__ == '__main__':
    pytest.main(["-s","test_autouse.py"])