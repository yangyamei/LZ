import urllib.request

#response响应常用的方法
url='http://demo.bxcker.com/customer/index.shtml'
headers={
"Host":"demo.bxcker.com",
"Connection":"keep-alive",
"Pragma":"no-cache",
"Accept":"*/*",
"X-Requested-With":"XMLHttpRequest",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
"Referer":"http://demo.bxcker.com/",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.9",
"Cookie":"MVC-JSESSIONID=DC898D6C534C956D2F3D44CF16C70188; SPRING_SECURITY_REMEMBER_ME_COOKIE=MXRPRnlrZStMT2ZHU1c3NDdzRkdDdz09OkJZWCt6cHZIdllNWFNVQlJUUmRTZUE9PQ"
}
request=urllib.request.Request(url,headers=headers)
response=urllib.request.urlopen(request)
html=response.read().decode('utf-8')
print(html)