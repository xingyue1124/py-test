import unittest
import os, datetime
from BeautifulReport import BeautifulReport

root_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')

report_dir = root_dir + '/test_report'

# 添加测试用例
test_dir = root_dir
discover = unittest.defaultTestLoader.discover(test_dir, 'beautiful*.py', None)

# 生成报告
now = datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')
filename = '测试报告' + str(now)
BeautifulReport(discover).report(description='测试', filename=filename, log_path=report_dir)
