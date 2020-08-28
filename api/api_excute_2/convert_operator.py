import json
import jsonpath
"""
1.首先，对body根据$切片
body='{"userid":$uservar.data[0].userid$,"openid":"$uservar.data[0].openid$","productid":$productvar.data[0].productid$}'

2.切片完成后，如下
{"userid":                   --索引为0
uservar.data[0].userid       --索引为1
,"openid":"                  --索引为2
uservar.data[0].openid       --索引为3
","productid":               --索引为4
productvar.data[0].productid --索引为5
}

3.拿到索引为奇数的：
uservar.data[0].userid
uservar.data[0].openid
productvar.data[0].productid

4.把变量取出来：
uservar
uservar
productvar

5.把jsonpath取出来：
data[0].userid
data[0].openid
data[0].productid

6.通过jsonpath在变量中取值：先将变量转换成json串，再用jsonpath取值

7.将取出来的值与原body中的自定义变量进行替换，再拼接起来，结果如下：
{"userid":17890,"openid":"UEHUXUXU78272SDSassDD","productid":8888}
"""
# body='{"userid":$uservar.data[0].userid$,"openid":"$uservar.data[0].openid$","productid":$productvar.data[0].productid$}'

# depend={
#             "uservar":'{"data":[{"nikename":"风清扬","openid":"UEHUXUXU78272SDSassDD","userbalance":5678.9,"userid":17890,"username":"admin","userpoints":4321}],"httpstatus":200}',
#             "productvar":'{"data":[{"SKU":"FRTSJ7676","price":29.9,"productdesc":"麒麟瓜皮薄瓜瓤嫩,就连翠衣也很清甜,瓤虽是粉红而不是深红,但甜度丝毫不减。","productid":8888,"productname":"海南麒麟瓜5斤装"}],"httpstatus":200}'
#           }

# 定义一个字典存放变量
depend = {}


class Convert:
    def convertOp(self, body):
        # 根据"$"切片
        listsplitvar = body.split("$")
        num = 0
        for strrequest in listsplitvar:
            # 等于1的时候就是要取得块
            if num % 2 == 1:
                # 拿到我要取的块
                strchuck = strrequest
                # 要把变量取出来
                envar = strchuck[0:strchuck.find(".")]
                # 变量拿出来
                varvalue = depend[envar]
                # 要把对应的jsonpath取出来
                varjsonpath = strchuck[strchuck.find(".") + 1:]
                # 通过jsonpath在变量里取值
                varjsonresult = json.loads(varvalue)
                varchuck = jsonpath.jsonpath(varjsonresult, expr="$." + varjsonpath)
                # 替换
                listsplitvar[num] = str(varchuck[0])
            # print(varjsonpath)
            num = num + 1
        listsplitvar = "".join(listsplitvar)
        print(listsplitvar)
        return listsplitvar

