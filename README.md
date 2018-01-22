# 微信小游戏《星途wegoing》刷分代码!
> 最近大家都在刷《跳一跳》的分数，排行榜已经全部沦为外挂的天下，刷多少分是个够呢。后来找到《星途wegoing》，分数玩不过别人，就开始动了歪心思。

* 程序默认刷233000分，要改分数请注意一定要改一个合理的分数。

* 如：总分数~=金币数量*300+(level-100)*200 以及combo的加成等。

* 多玩几把，然后算个合理的值。否则分数会被清0.


## 更新

* 2018-1-22 新增编译后的版本，windows平台的朋友如果没有python环境，可以直接下载exe执行。在[这里](https://github.com/Mocha-L/wechat_wegoing/tree/master/code)

* 2018-1-18 因游戏版本升级，为保证支持，更新代码；加入了证书不校验的参数，在抓包时也可以跑代码了

## 原理&步骤

1. 通过抓包分析《星途wegoing》的成绩上传报文
2. 分析JS查看各个参数的生成规则
3. 完成代码模拟仿真
4. 将抓包得到的sessionid拷贝出来，传给程序使用
5. 返回{"errcode":0,"errmsg":"ok","data":{"tile_list":[]}}即成功

## 效果

![](https://github.com/Mocha-L/wechat_wegoing/blob/master/image/my_score.png)

## 前提条件
* 掌握基本的抓包方法（如果有不会的看这里：[HTTPS抓包](http://mp.weixin.qq.com/s/JxJWZk-uMMjLcLQFTQ7thA)、[HTTPS抓包Fiddler4](http://mp.weixin.qq.com/s/dwJCfcPLY2Nxf_R8O4R__A)，如遇到证书验证导致无法抓包的问题的话看这个[安卓关闭证书验证](https://mp.weixin.qq.com/s/vA7u2f8NXiDW--IU50e_cQ)）
* 基础的python(3)知识等。

## 程序依赖库
  !!!python36
  
  requests

## 使用方法

1. 使用各种抓包工具抓取每局结束的时候的成绩上传报文，工具如Fiddler4、Charles、packet capture等均可。关键包如下：

![](https://github.com/Mocha-L/wechat_wegoing/blob/master/image/packet.png)

2. 将包体中的sessionid拷贝出来（该值短时间内有效）
3. 执行程序中的/code/run.py 文件，输入sessionid执行

# 特别说明

* 目前程序中的分数是我默认写死的，使用者可进行更改，但是最好分数符合游戏规律。
* 各个字段说明：
    
    * newscore（新成绩） 
      level（当前所在的星球数）根据js里所写，该值等于 100+你所跳的星球个数 
      baoshi（得到的宝石个数）
      combo（连击个数）
* 如果还有不明白的可以参考/game_package/wx7a727ff7d940bb3f.wxapkg.unpack/game.js文件，大致在1700行。如下：
![](https://github.com/Mocha-L/wechat_wegoing/blob/master/image/gamejs.png)

# 联系我
如果还有疑问，请通过以下方式联系我
* 提issues
* 关注微信公众号“燕幕自安”获取我的联系方式
* 加入我的QQ交流群（扫描下方二维码或搜索群号码579737590），大家帮助你解决问题

![QQ群](https://github.com/Mocha-L/wechat_wegoing/blob/master/image/qq.png)
![公众号](https://github.com/Mocha-L/Fitness_wxApp/blob/master/res/my_qr2.jpg)



