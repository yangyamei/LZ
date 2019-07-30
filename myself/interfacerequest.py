
from urllib import parse
import urllib.request
url='https://www.baidu.com/'
#定义一个字典
query={
    "query":"参数"
}
#urlencode()接受的参数是一个字典
pw=parse.urlencode(query)
print(pw)
