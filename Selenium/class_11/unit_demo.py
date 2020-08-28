import unittest
from selenium import webdriver
# 数据驱动测试模块导入:file_data解析yaml文件
from ddt import ddt, data, unpack, file_data
from time import sleep
import os
from Selenium.class_11.dict_value_demo import DictValueDemo

# 声明DDT的调用
@ddt
class UnitDemo(unittest.TestCase):

    # 通过yaml进行字典参数的传递
    '''
    [{'open_browser': {'loc': 'id', 'path': 'kw', 'txt': 'ceshi111'},
     'input': {'loc': 'id', 'path': 'su', 'txt': 'ceshi222'}}]
    '''

    @file_data('data.yaml')
    def test_01(self, **kwargs):
        d = DictValueDemo()
        d.test_dict(**kwargs['open_browser'])
        d.test_dict(**kwargs['input'])


if __name__ == '__main__':
    unittest.main()
