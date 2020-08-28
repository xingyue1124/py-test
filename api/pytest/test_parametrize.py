import pytest

@pytest.mark.parametrize("user",["user1","user2"])
def test_01(user):
    print(user)

if __name__ == '__main__':
    pytest.main(["-s","test_parametrize.py"])