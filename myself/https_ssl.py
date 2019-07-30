from urllib import parse
import urllib.request
import ssl
#表示忽略未经核实的ssl证书认证
context=ssl._create_unverified_context()
url='https://core.zsins.com/pcis//core/main.jsp'
headers={
    "User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,' 'like Gecko) Chrome/69.0.3497.100 Safari/537.36",
}
request=urllib.request.Request(url,headers=headers)
response=urllib.request.urlopen(request)
html=response.read().decode('utf-8')
print(html)