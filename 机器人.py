#coding:utf-8
import json
import urllib.request

#1、构建url
url = "添加机器人url"   #url为机器人的webhook

url1 = "添加机器人url"   #url为机器人的webhook
#
#2、构建一下请求头部
header = {
    "Content-Type": "application/json",
    "Charset": "UTF-8"
}
#3、构建请求数据
data = {
    "msgtype": "text",
    "text": {
        "content": "此处输入内容"
    },
    "at": {
        "isAtAll": False#@全体成员（在此可设置@特定某人）
    }
}

# 4、对请求的数据进行json封装
sendData = json.dumps(data)#将字典类型数据转化为json格式
sendData = sendData.encode("utf-8") # python3的Request要求data为byte类型

#5、发送请求
request = urllib.request.Request(url=url, data=sendData, headers=header)
request1 = urllib.request.Request(url=url1, data=sendData, headers=header)
# 6、将请求发回的数据构建成为文件格式

opener = urllib.request.urlopen(request)
opener = urllib.request.urlopen(request1)

#7、打印返回的结果
print(opener.read())
