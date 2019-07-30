import requests
from urllib import parse
url="http://demo.bxcker.com/qhiex_login"
headers={
"Accept":"application/json",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.9",
"Cache-Control":"no-cache",
"Connection":"keep-alive",
"Content-Length":"85",
"Content-Type":"application/x-www-form-urlencoded",
"Cookie":"MVC-JSESSIONID=2DBA21AFFF0CC5AA4EF2FD9C49139DCC",
"Host":"demo.bxcker.com",
"Origin":"http://demo.bxcker.com",
"Pragma":"no-cache",
"Referer":"http://demo.bxcker.com/",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
"X-Requested-With":"XMLHttpRequest"
}
data={
    "username":'demo100',
     "password": "demo100"
}
#通过URLcode()转码
post_data=parse.urlencode(data).encode(encoding="UTF8")
response=requests.post(url,headers=headers,data=post_data)
#返回cookiejar对象
cookiejar=response.cookies
cookiedict=requests.utils.dict_from_cookiejar(cookiejar)
print(cookiedict)
print(cookiejar)
#利用cookie登录，访问客户管理模块
r=requests.get("http://demo.bxcker.com/customer/index.shtml",headers=headers)
r.encoding='utf-8'
print(r.text)