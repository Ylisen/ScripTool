#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020-9-5 0:04
# @Author : lisen
# @File : send_email
# @Software: PyCharm
# @Contact : xxx.com
# @Desc :

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import argparse

my_sender = 'xxx@qq.com'  # 发件人邮箱账号
my_pass = 'fnhvjqbvsnrbhegd'  # 发件人邮箱授权码
to_user = 'xxx@qq.com'  # 收件人邮箱账号


def send_mail(subject, content):
    ret = True
    try:
        msg = MIMEText(content, 'plain', 'utf-8')  # 文本类型：plain、 html
        msg['Subject'] = subject  # 邮件的主题，也可以说是标题
        msg['From'] = formataddr(["lisen", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr([to_user, to_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [to_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:
        ret = False
    return ret


def parseargv():
    parser = argparse.ArgumentParser(description="发送微信")

    parser.add_argument('--title', '-t',
                        help='标题', )
    parser.add_argument('--msg', '-m',
                        help='消息',)
    argvs = parser.parse_args()
    return argvs


if __name__ == '__main__':
    argvs = parseargv()
    print(argvs.title, argvs.msg)
    ret = send_mail(argvs.title, argvs.msg)
    # ret = send_mail('test', 'i am yobhgfljd fgffgdr')
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
