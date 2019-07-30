import requests
kw={
    "kw":'电影'
}
headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
response=requests.get("http://www.baidu.com",headers=headers,params=kw)
#print(response.text)  #返回的是Unicode格式的数据
#print(response.content) #返回的是字节流数据
print(response.url)  #查看完整地址
print(response.status_code) #查看响应码