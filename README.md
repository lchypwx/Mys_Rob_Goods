# Mys_Goods_Rob 米游社商店兑换工具（云函数）  
## 使用说明  
* 上传代码包  
* 通过环境变量配置参数  
  * 根据`goods_list.py`所获取的信息填写所需商品的`goods_id`  
    * 会打包成`.exe`方便方便使用
  * 下文将详细说明`mys_cookies`,`goods_id`,`uid`,`address`,`server`,`biz`等参数的获取方法  
  * 通过配置`SCTkey`，可以使用Server酱的推送服务
* 测试能否正常运行  
* 配置定时触发器（cron表达式）  
* 部署完成，可以摸鱼了  

## 所需环境变量  
|  变量名  |  key  |  value  |  默认  |  value	获取方式  |
|  ----  | ----  | ----  | ----  | ----  |
|  商品id  |  goods_id  |  ----  | ----  | 必填，通过`good_list.py`获取，选择所需商品的id即可  |
|  米游社cookies  |  mys_cookies  |  ----  | ----  | 必填，详见获取方式  |
|  UID  |  uid  |  ----  | ----  | 必填，原神商品分区填原神uid，米游社商品分区填米游社id，未定，崩坏2，崩坏3同理  |
|  地址id  |  address  |  ----  | ----  | 代表你的收货地址，网页登录米游社后，点击[获取](https://api-takumi.mihoyo.com/account/address/list)，查看对应的id，一般为4位数  |
|  服务器  |  server  |  `cn_gf01`/`cn_qd01`  | cn_gf01  | 对应游戏的服务器，默认原神官服，此处仅列举原神，详见  |
|  兑换数量  |  exchange_num  |  ----  | 1  | 选填，小于兑换限制即可  |
|  商品分区  |  biz  |  `hk4e_cn`/`bh3_cn`/`bh2_cn`/`nxx_cn`  | hk4e_cn  | 必填，默认原神分区  |
|  Server酱  |  SCTkey  |  ----  | SCT  | 选填，前往[ServerChan](https://sct.ftqq.com/sendkey)官网登录获取  |
