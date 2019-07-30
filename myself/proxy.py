import urllib.request
url='http:www.baidu.com/'
header={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
#构建两个代理handler，一个有代理ip，一个每一代理ip
httpproxy_handler=urllib.request.ProxyHandler({"http":"61.135.217.7:80"})
nullproxy_handler=urllib.request.ProxyHandler({})
#定义一个代理开关
proxySwitch=True
#通过urllib.build_opener()方法使用这些代理Handler对象，创建自定义opener对象
if proxySwitch:
    opener=urllib.request.build_opener(httpproxy_handler)
else:
    opener=urllib.request.build_opener(nullproxy_handler)
request=urllib.request.Request(url,headers=header)
response=opener.open(request)