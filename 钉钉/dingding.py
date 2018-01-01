#coding:utf-8


import json
#import urllib
import urllib.request
import urllib.parse

#构建url
url ="https://oapi.dingtalk.com/robot/send?access_token=c471b1e031b39ebb4db5ff0b019da890c61391b9f0cb3322649ac3b5606dfea9"

#构建请求头部
header={
    "Content-Type":"application/json",
    "Charset":"utf-8"
}


#构建请求数据
data={
    "msgtype":"text",#代表传输的内容格式是一个文本
    "text":{
        "content":"hello world"
    },
    "at":{
        "atMobiles":[13712884027],#具体发给群里面的谁谁
       # "isAtAll":True#True/False是否群发
    }
    #"touser":"@all",`  +
    #"agentid":"4352760"

}

#对请求的数据json 封装
#data = json.dumps(data)#将字典格式数据转换为json形式
data = urllib.parse.urlencode(data).encode(encoding='UTF-8')

print(data)
#发送请求
request = urllib.request.Request(url=url,data=data,headers=header)#发起请求

#将请求返回的数据构建文件格式
opener = urllib.request.urlopen(request)

#打印返回的结果
print(opener.read().decode('utf-8'))


