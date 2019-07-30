import urllib.request
from urllib import parse
import pickle
url='https://www.baidu.com'
header={
    'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                 ' (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
keyword=input("请输入需要查询的字符串：")
wd={'wd':keyword}
wd=parse.urlencode(wd)
fullurl=url+"?"+wd
print(fullurl)
#url作为Request()方法的参数,构造并返回一个request对象
request=urllib.request.Request(fullurl,headers=header)
response=urllib.request.urlopen(request)
html=response.read().decode('utf-8')
with open('yym.txt','wb') as f:
    pickle.dump(html,f)