#import urllib.request
import urllib
from urllib import request
import random
import pickle
url='https://fanyi.baidu.com/'
header={
    'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                 'like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
#url作为request()的参数，构造并返回一个Request对象
request=urllib.request.Request(url)
#Request对象作为urlopen()方法的参数，发送给服务器并接受响应
#也可以通过调用request.add_header()添加/修改一个特定的header
request.add_header("Connection",'keep-alive')
#也可以通过reques.get_header()来查看header信息
print(request.get_header(header_name="Connection"))
response=urllib.request.urlopen(request)
html=response.read().decode('utf-8')
# with open('20190307.txt','wb') as f:
#     pickle.dump(html,f)
print(response.getcode())
print(response.geturl())
print(response.info())