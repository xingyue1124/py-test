import pytest
import requests
import json


# 前置信息，可用fixture标记
@pytest.fixture()
def userdata():
    username="admin"
    pwd="123456"
    return username,pwd


def test_login(userdata):
    username = userdata[0]
    password = userdata[1]
    url = "http://39.98.138.157:5000/api/login"
    data = {"username": username, "password": password}
    header = {"content-type": "application/json"}
    res = requests.post(url, data=json.dumps(data), headers=header)
    msg = res.json()["msg"]
    assert msg == "success"


if __name__ == '__main__':
    pytest.main(["-s", "test_fixture.py"])
