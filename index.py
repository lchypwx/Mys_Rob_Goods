# -*- coding: utf8 -*-
import os
import json
import time
import requests
def rob():
    url = "https://api-takumi.mihoyo.com/mall/v1/web/goods/exchange"
    headler = {
        "Host": "api-takumi.mihoyo.com",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://user.mihoyo.com",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; MuMu Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 miHoYoBBS/2.7.0",
        "x-rpc-client_type": "5",
        "x-rpc-device_id": "7dab6a2c-b917-4184-8da5-cffd45c085fc",
        "Referer": "https://user.mihoyo.com/?hideTitle=true&bbs_show_back=true",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,en-US;q=0.8",
        "Cookie": os.environ.setdefault("mys_cookies","23333")  # 米游社cookie
        }

    txt = {
        "app_id": "1",
        "point_sn": "myb",
        "goods_id": os.environ.setdefault("goods_id","2021102012224"),  # 商品id
        "exchange_num": os.environ.setdefault("exchange_num","1"),   #默认抢一个
        "uid": os.environ.setdefault("uid","1"),   # 米游社/游戏uid
        "region": os.environ.setdefault("server","cn_gf01"),  # 服务器
        "game_biz": os.environ.setdefault("biz","hk4e_cn"), 
        "address_id": os.environ.setdefault("address","1")  # 地址id 
    }
    r = requests.post(url=url,headers=headler,json=txt)
    msg=json.loads(r.text)
    recode=msg["retcode"]
    if recode==0:
        try:
            order_sn=msg["order_sn"]
        except(KeyError):
            order_sn=msg["data"]["order_sn"]
        try:
            message=msg['message']
        except(KeyError):
            message=msg["data"]['message']
    else:
        try:
            message=msg['message']
        except(KeyError):
            message=msg["data"]['message']
        order_sn=None
    
    return recode,message,order_sn

def send_msg(msg):
    url = "https://sctapi.ftqq.com/"+os.environ.setdefault("SCTkey","SCT")+".send"
    json = {
        "title":"米游社商店兑换简况",
        "desp":msg,
        }
    send=requests.post(url=url,params=json)
    return send.text

def good_name(id):
    url='https://api-takumi.mihoyo.com/mall/v1/web/goods/detail'
    headler={
    'Host': 'api-takumi.mihoyo.com',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://webstatic.mihoyo.com',
    'User-Agent': "Mozilla/5.0 (Linux; Android 6.0.1; MuMu Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 miHoYoBBS/2.7.0",
    'Referer': 'https://webstatic.mihoyo.com/app/community-shop/index.html?bbs_presentation_style=no_header',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,en-US;q=0.8',
    'Cookie': os.environ.setdefault("mys_cookies","23333"),
    'X-Requested-With': 'com.mihoyo.hyperion',
    }
    params={
    'app_id':'1',
    'point_sn':'myb',
    'goods_id':id
    }
    r=requests.get(url=url,headers=headler,params=params)
    msg=json.loads(r.text)
    msg=msg['data']
    try:
        url=msg['cover'][-1]['url']
    except(KeyError):
        url=None
    try:
        return msg['goods_name'],url
    except(TypeError):
        return None

def main_handler(event, context):
    start=time.time()
    start_t=time.ctime()
    for times in range(100): #请求次数
        msg=rob()
        times+=1
        if msg[0]==0 or msg[0]==-2109 or msg[0]==-2007 or msg[0]==-2103:
            break
    good_n=good_name(os.environ.setdefault("goods_id","1"))
    
    s_msg='''
## {}—
## {}  
> 耗时：{:.5f}   
***
```
目标商品：{}  
retcode：{}  
message：{}  
订单号：{}  
请求次数：{}
```
![Image]({})
    '''.format(start_t,time.ctime(),time.time()-start,good_n[0],msg[0],msg[1],msg[2],times,good_n[-1])
    send_msg(s_msg)
    return s_msg