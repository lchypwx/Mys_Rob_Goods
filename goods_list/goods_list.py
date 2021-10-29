import json
import requests
pages=20 
good_type=['bh3','hk4e','bh2','nxx','bbs']
good_dict={'':'全部商品','bh3':'崩坏三','hk4e':'原神','bh2':'崩坏二','nxx':'未定事件簿','bbs':'米游社'}
url='https://api-takumi.mihoyo.com/mall/v1/web/goods/list'
headler={
'Host': 'api-takumi.mihoyo.com',
'Connection': 'keep-alive',
'Accept': 'application/json, text/plain, */*',
'Origin': 'https://user.mihoyo.com',
'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; MI NOTE Pro Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36 miHoYoBBS/2.12.1',
'x-rpc-client_type': '5',
'x-rpc-device_id': '58cb65c8-463f-4503-8389-cd2ff1d7d36f',
'Referer': 'https://webstatic.mihoyo.com/app/community-shop/index.html?bbs_presentation_style=no_header',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,en-US;q=0.8',
'Cookie': '', 
'X-Requested-With': 'com.mihoyo.hyperion'
}
print('\n==============商品id列表-goods_id list=====================')
for good_t in good_type:
    for page in range(pages):
        page+=1
        params={
        'app_id':'1',
        'point_sn':'myb',
        'page_size':'20',
        'page':str(page),
        'game':good_t
        }
        r=requests.get(url=url,headers=headler,params=params)
        msg=json.loads(r.text)
        msg=msg['data']
        msg=msg['list']
        good_id=[]
        good_name=[]
        for good in msg:
            good_id.append(good['goods_id'])
            good_name.append(good['goods_name'])
        ziped=zip(good_id,good_name)
        print('类型：'+good_t+'\n游戏：'+good_dict[good_t])
        hs=0
        for msg in ziped:
            hs+=1
            print(msg,end='\t\t\t')
            if hs%1==0:
                print()
        if msg==[]:
            break
left=input('Enter关闭...')