import requests
import json
from pyparsing import unicode


def Post_api():
    # 接口URL，请求体和请求头信息
    url = 'http://39.98.138.157:5000/api/login'
    data = {"username": "admin", "password": "123456"}
    header = {"content-type": "application/json"}

    # 两种发送请求的方式
    res = requests.request('post', url, headers=header, data=json.dumps(data))
    # res = requests.post(url, headers=header, data=json.dumps(data))

    # print(res.status_code)  # 状态码
    # print(res.content)  # 字节类型
    print(type(res.text),res.text)  # 字符串类型
    resp = res.text
    resp = json.loads(resp)  # 把json字符串转换成python中的字典形式
    print('转换之后的类型',type(resp),resp)
    # print(res.json())  # 字典类型
    # print(res.headers)  # 返回头信息
    # print(res.apparent_encoding)  # 编码格式

    # 获取返回值里面的token
    token = res.json()['token']
    print(token)

# 运行
Post_api()


# def Get_api():
#
#     params = {"productid":8888}
#     res = requests.get("http://39.98.138.157:5000/api/getproductinfo",params=params)
#     # 也可在URL中输入完整请求
#     # res = requests.get("http://39.98.138.157:5000/api/getproductinfo?productid=8888")
#     print(res.json())
#     print(json.loads(res.content))  # 若直接打印content商品详情会以Unicode形式输出
#     print(unicode(res.content,'unicode_escape'))  # 或者使用Unicode转义
#
# Get_api()