import requests
import json
import pytest


# 定义fixture的级别为session
@pytest.fixture(scope="session")
def get_token():
    url = "http://39.98.138.157:5000/api/login"
    data = {"username": "admin", "password": "123456"}
    header = {"content-type": "application/json"}
    res = requests.post(url, data=json.dumps(data), headers=header)
    token = res.json()["token"]
    print("this is session py")
    return token
