> 吐司签到+主机IP报告脚本，附带发送邮箱，可通过发送邮箱的方式，微信提醒

```
场景： 在外得知家里服务器公网IP
愿景： 不想食用DDNS(例如aliyun dns等, 暴露个人信息)
做法： 直接跟吐司签到脚本结合, 邮箱发送
```
利用crontab每日定时发送Email
> 每天8点半来个简略报告
```
30 8 * * * python /root/tools/sign.py >> /root/tools/logs_sign.log 2>&1
```

eg.
[!example.png]