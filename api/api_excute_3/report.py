import unittest
from HTMLTestRunner import HTMLTestRunner
from datetime import datetime
from api.api_excute_3.send_mail import sendmail


class report:
    def toReport(self):
        # 报告格式化名称
        time = datetime.now()
        now = time.strftime('%Y-%m-%d %H-%M-%S')
        # 报告的路径
        report_path = './' + now + 'result.html'

        with open(report_path, 'wb') as f:
            runner = HTMLTestRunner(stream=f, verbosity=2, title="ddt接口测试报告", description="接口测试报告信息")
            runner.run(unittest.defaultTestLoader.discover("", pattern="main.py"))

        f.close()
        # 邮件发送
        sendmail().send_mail(report_path)


if __name__ == '__main__':
    report().toReport()
