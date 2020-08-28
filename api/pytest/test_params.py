import pytest

user_data = ['user1', 'user2']


@pytest.fixture(scope="function", params=user_data, ids=["test1", "test2"])
def users(request):
    return request.param


def test_register(users):
    print("用户：%s" % users)


if __name__ == '__main__':
    pytest.main(["-s", "test_params.py"])
