# 实现对邮件进行发送
import smtplib

# email实现邮件构建
from email.mime.text import MIMEText
from email.header import Header

# 如何实现文本邮件的发送,plain指的就是纯文本类型
message=MIMEText(_text="python课程 纯文本邮件发送",_subtype='plain',_charset="utf-8")
# 指定发件人，收件人和主题
message["From"]=Header("发件人","utf-8")
message["To"]=Header("收件人","utf-8")
message["Subject"]=Header("主题：Python纯文本邮件","utf-8")
# 创建一个实例化对象
smtpobj=smtplib.SMTP()

# qq的smtp服务器地址
mail_host="smtp.qq.com"

try:
    # 连接smtp服务器
    smtpobj.connect(host=mail_host,port="587")

    # 用户登录,用户名即为发送者地址，密码不是账号的密码，是授权码
    smtpobj.login(user="544598571@qq.com",password="kvdotsnkkfgbbbhg")
    # 如何获取授权码  发送者邮件点击设置-账户-开启pop3/smtp协议 获取授权码

    sender="544598571@qq.com"
    receiver=["544598571@qq.com"]
    # 实现邮件发送
    smtpobj.sendmail(sender,receiver,message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("邮件发送失败！")



# # 实现对邮件进行发送
# import smtplib
#
# # email实现邮件构建
# from email.mime.text import MIMEText
# from email.header import Header
#
# # html文件
# html="""
# <p>python HTML邮件发送</p>
# <p><a href="https://www.baidu.com">百度</a>
# </p>
# """
# message=MIMEText(_text=html,_subtype='html',_charset="utf-8")
#
# # 指定发件人，收件人和主题
# message["From"]=Header("发件人","utf-8")
# message["To"]=Header("收件人","utf-8")
# message["Subject"]=Header("主题：Python基于HTML邮件","utf-8")
# # 创建一个实例化对象
# smtpobj=smtplib.SMTP()
#
# # qq的smtp服务器地址
# mail_host="smtp.qq.com"
#
# try:
#     # 连接smtp服务器
#     smtpobj.connect(host=mail_host,port="587")
#
#     # 用户登录,用户名即为发送者地址，密码不是账号的密码，是授权码
#     smtpobj.login(user="544598571@qq.com",password="kvdotsnkkfgbbbhg")
#     # 如何获取授权码  发送者邮件点击设置-账户-开启pop3/smtp协议 获取授权码
#
#     sender="544598571@qq.com"
#     receiver=["544598571@qq.com"]
#     # 实现邮件发送
#     smtpobj.sendmail(sender,receiver,message.as_string())
#     print("邮件发送成功")
# except smtplib.SMTPException:
#     print("邮件发送失败！")



# # 实现对邮件进行发送
# import smtplib
#
# # email实现邮件构建
# from email.mime.text import MIMEText
# from email.header import Header
# # 实现附件
# from email.mime.multipart import MIMEMultipart
# message=MIMEMultipart()
# message.attach(MIMEText("附件邮件测试",_subtype="plain",_charset="utf-8"))
#
# att1=MIMEText(open("test.txt","rb").read(),"base64","utf-8")
# att1["Content-Type"] = 'application/octet-stream'
# # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# att1["Content-Disposition"] = 'attachment; filename="1.txt"'
# message.attach(att1)
#
# # 继续添加一个文件为附件
# att2 = MIMEText(open('2.txt', "rb").read(), "base64", "utf-8")
# att2["Content-Type"] = 'application/octet-stream'
# # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# att2["Content-Disposition"] = 'attachment; filename="2.txt"'
# message.attach(att2)
#
# # 指定发件人，收件人和主题
# message["From"]=Header("发件人","utf-8")
# message["To"]=Header("收件人","utf-8")
# message["Subject"]=Header("主题：Python发送带附件邮件","utf-8")
# # 创建一个实例化对象
# smtpobj=smtplib.SMTP()
#
# # qq的smtp服务器地址
# mail_host="smtp.qq.com"
#
# try:
#     # 连接smtp服务器
#     smtpobj.connect(host=mail_host,port="587")
#
#     # 用户登录,用户名即为发送者地址，密码不是账号的密码，是授权码
#     smtpobj.login(user="544598571@qq.com",password="kvdotsnkkfgbbbhg")
#     # 如何获取授权码  发送者邮件点击设置-账户-开启pop3/smtp协议 获取授权码
#
#     sender="544598571@qq.com"
#     receiver=["544598571@qq.com"]
#     # 实现邮件发送
#     smtpobj.sendmail(sender,receiver,message.as_string())
#     print("邮件发送成功")
# except smtplib.SMTPException:
#     print("邮件发送失败！")