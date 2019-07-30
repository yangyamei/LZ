#cookielib  HTTPCookirProcessor  http.cookiejar和HTTPCookieProcessor处理器
import urllib.request
import http.cookiejar
from urllib import parse
#构建一个CookieJar对象实例来保存cookie
cookie=http.cookiejar.CookieJar()
#使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
cookie_handler=urllib.request.HTTPCookieProcessor(cookie)
#通过build_opener()来构建opener
opener=urllib.request.build_opener(cookie_handler)
headers={
"Referer": "http://demo.bxcker.com/",

"Connection": "keep-alive",

"X-Requested-With": "XMLHttpRequest",

"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",

"Content-Type": "application/x-www-form-urlencoded",

"Accept-Language": "zh-CN,zh;q=0.9"
}
#登录的账户名和密码
data={"username":"demo100","password":"demo100"}
#通过urlencode()转码
postdata=parse.urlencode(data).encode(encoding="UTF8")
#构建Request请求对象，包含需要发送的用户名和密码
request=urllib.request.Request("http://demo.bxcker.com/qhiex_login",data=postdata)
#通过opener发送请求，并获取登录后的cookie值
opener.open(request)
#opener包含用户登录后的cookie值，可直接访问那些登录后才能访问的页面
response=opener.open("http://demo.bxcker.com/customer/index.shtml")
print(response.read().decode("utf-8"))