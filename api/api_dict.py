import unittest
import requests
import json
import jsonpath


class MyTestCase(unittest.TestCase):
    # 定义一个字典，存储所有变量
    vardict = {}

    def test_1login(self):
        url = "http://39.98.138.157:5000/api/login"
        data = {"username": "admin", "password": "123456"}
        header = {"content-type": "application/json"}
        # json.dumps：将字符串转换为json串
        res = requests.post(url, headers=header, data=json.dumps(data))
        resjson = res.json()
        print(resjson)
        # 将返回值存在字典中
        MyTestCase.vardict["login"] = resjson
        # 断言msg
        msg = jsonpath.jsonpath(resjson, "$.msg")[0]
        self.assertEqual("success", msg)

    def test_2userinfo(self):
        url = "http://39.98.138.157:5000/api/getuserinfo"
        # 使用dict的变量取值
        token = jsonpath.jsonpath(MyTestCase.vardict["login"], "$.token")[0]
        header = {"token": token}
        res = requests.get(url, headers=header)
        resjson = res.json()
        print(resjson)
        # 将返回值存在字典中
        MyTestCase.vardict["userinfo"] = resjson
        # 断言httpstatus
        httpcode = jsonpath.jsonpath(resjson, "$.httpstatus")[0]
        self.assertEqual(200, httpcode)

    def test_3productinfo(self):
        url = "http://39.98.138.157:5000/api/getproductinfo?productid=8888"
        res = requests.get(url)
        resjson = res.json()
        print(resjson)
        # 将返回值存在字典中
        MyTestCase.vardict["productinfo"] = resjson
        # 断言
        httpcode = jsonpath.jsonpath(resjson, "$.httpstatus")[0]
        self.assertEqual(200, httpcode)

    def test_4addcart(self):
        url = "http://39.98.138.157:5000/api/addcart"
        # 使用dict的变量取值
        token = jsonpath.jsonpath(MyTestCase.vardict["login"], "$.token")[0]
        userid = jsonpath.jsonpath(MyTestCase.vardict["userinfo"], "$.data[0].userid")[0]
        openid = jsonpath.jsonpath(MyTestCase.vardict["userinfo"], "$.data[0].openid")[0]
        productid = jsonpath.jsonpath(MyTestCase.vardict["productinfo"], "$.data[0].productid")[0]
        header = {"token": token, "content-type": "application/json"}
        data = {"userid": userid, "openid": openid, "productid": productid}
        data = json.dumps(data)
        res = requests.post(url, headers=header, data=data)
        resjson = res.json()
        print(resjson)
        # 将返回值存在字典中
        MyTestCase.vardict["addcart"] = resjson
        # 断言
        httpcode = jsonpath.jsonpath(resjson, "$.httpstatus")[0]
        self.assertEqual(200, httpcode)

    def test_5createorder(self):
        url = "http://39.98.138.157:5000/api/createorder"
        token = jsonpath.jsonpath(MyTestCase.vardict["login"], "$.token")[0]
        userid = jsonpath.jsonpath(MyTestCase.vardict["userinfo"], "$.data[0].userid")[0]
        openid = jsonpath.jsonpath(MyTestCase.vardict["userinfo"], "$.data[0].openid")[0]
        productid = jsonpath.jsonpath(MyTestCase.vardict["productinfo"], "$.data[0].productid")[0]
        cartid = jsonpath.jsonpath(MyTestCase.vardict["addcart"], "$.data[0].cartid")[0]
        header = {"token": token, "content-type": "application/json"}
        data = {"cartid": cartid, "openid": openid, "productid": productid,
                "userid": userid}
        data = json.dumps(data)
        res = requests.post(url, headers=header, data=data)
        resjson = res.json()
        print(resjson)
        # 断言
        httpcode = jsonpath.jsonpath(resjson, "$.httpstatus")[0]
        self.assertEqual(200, httpcode)


if __name__ == '__main__':
    unittest.main()
