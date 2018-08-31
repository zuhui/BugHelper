import smtplib
import os
from email.header import Header
from email.mime.text import MIMEText



def send_mail():

    #设置发件人和收件人
    sender = '发件人邮箱'
    receiver = '收件人邮箱'

    #所使用的用来发送邮件的SMTP服务器
    smtpServer = 'smtp.qq.com'

    # 发送邮箱的用户名和授权码（不是登录邮箱的密码）
    username = '帐号'
    password = '密码'

    # 邮件主题
    mail_title = '主题：每日BUG状态报告'

    # 读取html文件内容

    f = open(getLastReport(), 'rb')  # HTML文件默认和当前文件在同一路径下，若不在同一路径下，需要指定要发送的HTML文件的路径
    mail_body = f.read()
    f.close()

    # 邮件内容, 格式, 编码
    message = MIMEText(mail_body, 'html', 'utf-8')
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header(mail_title, 'utf-8')

    try:
        smtp = smtplib.SMTP_SSL(smtpServer,465)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, message.as_string())
        print("发送邮件成功！！！")
        smtp.quit()
    except smtplib.SMTPException:
        print("发送邮件失败！！！")

def getLastReport():

    lists = os.listdir("files/")
    lists.sort(key = lambda fn:os.path.getmtime("files/" +"\\"+fn)) #按时间排序

    file_new = os.path.join("files/",lists[-1])
    print(file_new)

    return file_new

'''
if __name__ == "__main__":
    send_mail()
'''

