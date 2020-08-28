import unittest
from ddt import ddt, data, unpack
from api.api_excute_2.excel_operator import excelData
from api.api_excute_2.operator_common import operator_Common
import jsonpath
from api.api_excute_2.convert_operator import Convert, depend


@ddt
class MyTestCase(unittest.TestCase):

    @data(*excelData().getExcel())
    @unpack
    def test_get_commonapi(self, url, body, header, method, method_type, expectvalue, jsonpathvalue, dependency):
        common = operator_Common()
        # 三元运算符：如果body为None则传入空，否则传入对应值
        body = "" if body is None else body
        header = "" if header is None else header
        # 用例中，如果body或header中找到$，则调用Convert类进行转换
        body = Convert().convertOp(body) if body.find("$") >= 0 else body
        header = Convert().convertOp(header) if header.find("$") >= 0 else header

        res = common.request(method, url, method_type, body, header)
        # 如果dependency的长度>0，且不为/，则存入变量
        if len(dependency) > 0 and dependency.find("/") < 0:
            depend[dependency] = res.content

        print(res.json())
        code = res.status_code
        jsonpathexcept = jsonpath.jsonpath(res.json(), jsonpathvalue)
        self.assertEqual(expectvalue, jsonpathexcept[0])
