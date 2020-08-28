# 框架数据驱动核心方法
import json
import jsonpath
import pytest
from api.api_auto_framework_pytest.tools.log import logger
from api.api_auto_framework_pytest.tools.operatorexcel import excelData
from api.api_auto_framework_pytest.requestcommon.request_common import request_Common
from api.api_auto_framework_pytest.tools.convertoperator import operatorConvert, depend


class Test_Case:

    @pytest.mark.parametrize("case", excelData().get_excel_data())
    def test_commonapi(self, case):
        print(case)
        url = case[0]
        body = case[1]
        header = case[2]
        method = case[3]
        method_type = case[4]
        expect = case[5]
        jsonpaths = case[6]
        dependency = case[7]

        logger.info("用例数据拆包开始。。。。")
        print(url + "-" + str(body) + "-" + str(
            header) + "-" + method + "-" + method_type + "-" + str(expect) + "-" + jsonpaths + "-" + dependency)
        common = request_Common()
        logger.info("替换body中的空格换行特殊字符开始。。。。")
        body = body.replace('\r', '').replace('\n', '').replace('\t', '') if body is not None else ""

        logger.info("转换存在可变变量开始。。。。")
        # 假如body中存在变量获取符号，调用convertBody重新对变量进行转化
        body = operatorConvert().convertBody(body) if body.find('$') >= 0 else body
        header = operatorConvert().convertBody(header) if (header is not None and header.find('$') >= 0) else header
        header = "" if header is None else header
        res = common.request(method, url, method_type, body, header)

        # 判断dependency是否有值需要存储
        if len(res.content) > 0 and dependency.find('/') < 0:
            depend[dependency] = res.content

        # 获取请求返回值
        resjson = json.loads(res.content)

        # 获得预期jsonpath路径下的值
        result = jsonpath.jsonpath(resjson, expr=jsonpaths)

        # 断言预期值和实际返回值对比
        assert expect.strip() == str(result[0])
