import smtplib
from email.mime.text import MIMEText


class sendmail:

    def send_mail(self, path):
        # 定义读文件
        f = open(path, 'rb')
        # 直接读到mailbody
        mail_body = f.read()
        f.close()

        # 邮件发送服务器
        host = "smtp.qq.com"
        # 端口
        port = 465
        # 发送邮件人
        sender = "544598571@qq.com"
        # 发送密码
        pwd = "hulkitgzkojibehh"

        revceiver = "544598571@qq.com"

        msg = MIMEText(mail_body, 'HTML', 'UTF-8')

        msg['subject'] = 'ddt自动化报告'
        msg['from'] = sender
        msg['to'] = revceiver

        s = smtplib.SMTP_SSL(host, port)
        s.login(sender, pwd)
        s.sendmail(sender, revceiver, msg.as_string())
