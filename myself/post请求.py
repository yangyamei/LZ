import urllib.request
from urllib import parse
url='http://fy.iciba.com/ajax.php?a=fy'
#请求头
headers={
   'Accept':'application/json',
   # 'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
}
key=input("请输入需要翻译的文字：")
form_data={
    'f':'auto',
    't':'auto',
    'w':'语文'
}
form_data=parse.urlencode(form_data).encode(encoding='UTF8')
#如果Request()方法里的data参数有值，那么这个请求就是post，如果没有，就是Get
request=urllib.request.Request(url,data=form_data,headers=headers)
response=urllib.request.urlopen(request)
html=response.read().decode('utf-8')
print(html)