#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/16 14:01
# @Author  : le31ei
# @File    : auto_sign.py
import requests
import smtplib
from email.mime.text import MIMEText

session = requests.session()
req_header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
}


def login():
    login_url = 'https://www.t00ls.net/login.json'
    login_data = {
        'action': 'login',
        'username': 'xx',
        'password': 'xx',
        'questionid': 3,
        'answer': 'xx'
    }
    resp = session.post(login_url, data=login_data, headers=req_header)
    if resp.json()['status'] == 'success':
        return resp.json()['formhash']
    else:
        raise Exception('登录失败')

def sign(formhash):
    sign_url = 'https://www.t00ls.net/ajax-sign.json'
    sign_data = {
        'formhash': formhash,
        'signsubmit': 'true'
    }
    resp = session.post(sign_url, data=sign_data, headers=req_header)
    if resp.json()['status'] == 'success':
        print('签到成功')
        send_mail('签到成功')
    else:
        send_mail('签到失败: {}'.format(resp.json()['message']))
        print('签到失败：{}'.format(resp.json()['message']))


def send_mail(title, content=''):
    mail_pass = 'xxx'
    mail_name = 'xxx'
    mail_host = 'smtp.163.com'
    sender = 'xx@163.com'
    receivers = ['xx@qq.com']
    message = MIMEText(content)
    message['Subject'] = title
    message['From'] = sender
    message['To'] = receivers[0]
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host)
        smtpObj.login(mail_name, mail_pass)
        smtpObj.sendmail(
            sender, receivers, message.as_string())
        smtpObj.quit()
        print('发送成功')
    except smtplib.SMTPException as e:
        print('error', e)



def main():
    formhash = login()
    sign(formhash)


if __name__ == '__main__':
    main()
