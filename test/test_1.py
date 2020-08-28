# # 实现对邮件进行发送
# import smtplib
#
# # email实现邮件构建
# from email.mime.text import MIMEText
# from email.header import Header
#
# # 如何实现文本邮件的发送,plain指的就是纯文本类型
# message=MIMEText(_text="python课程 纯文本邮件发送_邢月0086",_subtype='plain',_charset="utf-8")
# # 指定发件人，收件人和主题
# message["From"]=Header("发件人","utf-8")
# message["To"]=Header("收件人","utf-8")
# message["Subject"]=Header("主题：Python纯文本邮件_邢月0086","utf-8")
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
#     receiver=["2804555260@qq.com"]
#     # 实现邮件发送
#     smtpobj.sendmail(sender,receiver,message.as_string())
#     print("邮件发送成功")
# except smtplib.SMTPException:
#     print("邮件发送失败！")



# 实现对邮件进行发送
import smtplib

# email实现邮件构建
from email.mime.text import MIMEText
from email.header import Header
# 附件邮件
from email.mime.multipart import MIMEMultipart
message=MIMEMultipart()
message.attach(MIMEText("附件邮件测试，一个英文名称附件，一个中文名称附件",_subtype="plain",_charset="utf-8"))

att1=MIMEText(open("test.txt","rb").read(),"base64","utf-8")
att1["Content-Type"] = 'application/octet-stream'
# 附件名为英文
att1["Content-Disposition"] = 'attachment; filename="jiaoben.txt"'
message.attach(att1)

# 继续添加一个文件为附件，附件名称为中文
att2 = MIMEText(open('test.txt', "rb").read(), "base64", "utf-8")
att2["Content-Type"] = 'application/octet-stream'
# 附件名称为中文时的写法
att2.add_header("Content-Disposition", "attachment", filename=("gbk", "", "脚本.txt"))
message.attach(att2)


# 指定发件人，收件人和主题
message["From"]=Header("发件人","utf-8")
message["To"]=Header("收件人","utf-8")
message["Subject"]=Header("主题：Python发送带附件邮件_邢月0086","utf-8")
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

