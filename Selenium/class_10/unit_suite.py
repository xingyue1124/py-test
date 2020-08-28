import unittest
from Selenium.class_10.unit_taojian import UnitDemo
# 导入HTMLTestRunner
from HTMLTestRunner import HTMLTestRunner
import os

# 套件与运行器的操作


# 添加用例：总计5种方式
# # 添加1：基于用例名称进行添加
# suite.addTest(UnitDemo('test_case01'))
# # 添加2：基于用例名称添加多条测试用例
# cases= [UnitDemo('test_case02'), UnitDemo('test_case05'),UnitDemo('test_case04')]
# suite.addTests(cases)
# 添加3：基于指定路径，依照文件名称匹配对应的UnitTest来执行
# test_dir = '../class_10/'
# discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='unit_taojian.py')
# 若要执行多个文件，且文件名成类似，可将pattern='unit_taojian.py'修改为pattern='unit_t*.py'
# 添加4：指定的类对象中所有的测试用例
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(UnitDemo))
# 添加5：基于指定名称的类对象的所有测试用例（在一个路径下要加文件名，不在一个路径下要加包名）
# suite.addTests(unittest.TestLoader().loadTestsFromName('unit_taojian.UnitDemo'))

# 运行器：套件的运行需要结合运行器来执行，默认使用TextTestRunner
# runner= unittest.TextTestRunner()
# runner.run(suite)



# 创建一个测试报告运行器，生成一个.html文件
report_name = '测试报告名称'
report_title = '测试报告标题'
report_desc = '测试报告描述详情'
# 保存路径
report_path = './report_html/'
# 保存文件名称及位置
report_file = report_path + 'report.html'
# 判断report_path是否存在，如果不存在，新增
if not os.path.exists(report_path):
    os.mkdir(report_path)
else:
    pass

# 生成测试报告
with open(report_file,'wb') as report:
    # 创建一个套件：可以理解为是一个list，用于存放测试用例
    suite = unittest.TestSuite()
    suite.addTest(UnitDemo('test_case01'))
    suite.addTest(UnitDemo('test_case02'))
    htmlrunner = HTMLTestRunner(stream=report, title=report_title, description=report_desc)
    htmlrunner.run(suite)


