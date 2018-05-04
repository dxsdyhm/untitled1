from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# 图片和视频消息立马转发给自己
# 文本或者链接消息存入数据库

# 导入模块
from wxpy import *
import datetime
from wechat import models
from wechat.models import wxInfo
# 初始化机器人，扫码登陆
bot = Bot(console_qr=True)

@bot.register()
def saveMessage(msg):
    print(msg)
    now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if msg.type==TEXT:
        print('文本消息保存数据库')
        wxMessage=wxInfo(type=TEXT,text=msg.text,frome=msg.sender,time=now)
        wxMessage.save()
    elif msg.type==VIDEO:
        print('change massage to myself')
    else:
        print('pass')

def stopwechat(request):
    bot.logout()
    return HttpResponse('logout')

bot.join()

