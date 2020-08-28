import unittest
from ddt import ddt, data, unpack
from api.api_excute.excel_operator import excelData
from api.api_excute.operator_common import operator_Common
import jsonpath


@ddt
class MyTestCase(unittest.TestCase):

    @data(*excelData().getExcel())
    @unpack
    def test_get_commonapi(self, url, body, header, method, method_type, expectvalue, jsonpathvalue):
        common = operator_Common()
        # 三元运算符：如果body为None则传入空，否则传入对应值
        body = "" if body is None else body
        header = "" if header is None else header
        res = common.request(method, url, method_type, body, header)
        print(res.json())
        code = res.status_code
        jsonpathexcept = jsonpath.jsonpath(res.json(), jsonpathvalue)
        self.assertEqual(expectvalue, jsonpathexcept[0])
