# Mys_Goods_Rob 米游社商店兑换工具（云函数）  
## 使用说明  
* 上传代码包  
* 通过[环境变量](https://github.com/TuanKay10/Mys_Goods_Rob#%E6%89%80%E9%9C%80%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F)配置参数  
  * 根据`goods_list.py`所获取的信息填写所需商品的`goods_id`  
    * 会打包成`.exe`方便方便使用
  * 下文将详细说明`mys_cookies`,`goods_id`,`uid`,`address`,`server`,`biz`等参数的获取方法  
  * 通过配置`SCTkey`，可以使用Server酱的推送服务
* 测试能否正常运行  
* 配置定时触发器（cron表达式）  
* 部署完成，可以摸鱼了  
## Cookies获取  

## 所需环境变量  
|  变量名  |  key  |  value  |  默认  |  value	获取方式  |
|  ----  | ----  | ----  | ----  | ----  |
|  商品id  |  goods_id  |  ----  | ----  | 必填，通过`good_list.py`获取，选择所需商品的id即可  |
|  米游社cookies  |  mys_cookies  |  ----  | ----  | 必填，详见[Cookies获取](https://github.com/TuanKay10/Mys_Goods_Rob#cookies%E8%8E%B7%E5%8F%96)  |
|  UID  |  uid  |  ----  | ----  | 必填，原神商品分区填原神uid，米游社商品分区填米游社id，未定，崩坏2，崩坏3同理  |
|  地址id  |  address  |  ----  | ----  | 代表你的收货地址，网页登录米游社后，点击[获取](https://api-takumi.mihoyo.com/account/address/list)，查看对应的id，一般为4位数  |
|  服务器  |  server  |  `cn_gf01`/`cn_qd01`  | `cn_gf01`  | 对应游戏的服务器，默认原神官服，此处仅列举原神，详见[服务器名](https://github.com/TuanKay10/Mys_Goods_Rob#%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%90%8D)  |
|  兑换数量  |  exchange_num  |  ----  | 1  | 选填，小于兑换限制即可  |
|  商品分区  |  biz  |  `hk4e_cn`/`bh3_cn`/`bh2_cn`/`nxx_cn`  | `hk4e_cn`  | 必填，默认原神分区  |
|  Server酱  |  SCTkey  |  ----  | SCT  | 选填，前往[ServerChan](https://sct.ftqq.com/sendkey)官网登录获取  |
## 服务器名（待补充）
|  名称  |  服务器名  |  商品分区  |
|  ----  | ----  | ----  |
|  米游社  | ----  | bbs  |
|  原神  | `cn_gf01`(官服)/`cn_qd01`（渠道服，如b服，小米服）  | hk4e_cn  |
|  崩坏三  | `android01`(安卓1服)/`pc01`(桌面服)  | bh3_cn  |
|  崩坏二  | `gf01`(国服01)  | bh2_cn  |
|  未定事件簿  | `cn_prod_gf01`(官方服)  | nxx_cn  |
