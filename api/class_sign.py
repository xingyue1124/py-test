import hashlib
from datetime import datetime
import requests


class signmethod:
    def signmake(self):
        # appkey
        appkey = "e3d0428dd0b1459495012aff834746ed"
        # 请求url
        url = "https://route.showapi.com/64-19?com=yuantong&nu=YT4620020577123&showapi_appid=298130&showapi_timestamp={{time}}&showapi_sign={{sign}}"
        # 生成数组把？后面的&分裂，排成一个list
        params = url.split("?")[1].split("&")
        print(params)
        #
        if len(params) > 0:
            str_parm = ""
            # 时间格式生成showapi_timestamp
            timereplace = datetime.now().strftime("%Y%m%d%H%M%S")
            for p in sorted(params):
                # 如果是showapi_sign  不参与签名
                if p.split("=")[0] == "showapi_sign":
                    continue
                # 如果是showapi_timestamp  我就要重新赋值now给他
                if p.split("=")[0] == "showapi_timestamp":
                    now = timereplace
                    str_parm += p.split("=")[0] + now
                else:
                    # 要参与签名的其他参数
                    str_parm += p.split("=")[0] + p.split("=")[1]
            # 拼装一个密钥加在后面
            str_parm += appkey
            print(str_parm)
            # 生成MD5sign
            sign = hashlib.md5(str_parm.encode()).hexdigest()
            # 替换两个参数
            url = url.replace("{{time}}", timereplace)
            url = url.replace("{{sign}}", sign)
            print(url)
            res = requests.request("POST", url)

            print(res.json())

if __name__ == '__main__':
    signmethod().signmake()