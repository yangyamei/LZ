import requests
from bs4 import BeautifulSoup
from lxml import etree

url='http://127.0.0.1:8090/recruit.students/login/in?'
headers={
"Connection":"keep-alive",
# "Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
# "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Referer":"http://127.0.0.1:8090/recruit.students/login/view"
}
payload={
    "account":"admin",
    "pwd":"660B8D2D5359FF6F94F8D3345698F88C"
}

response=requests.get(url,headers=headers,params=payload)
html=etree.HTML(response.text)
# soup=BeautifulSoup(html,"lxml")
# info=soup.select('.toprighthref')[0].get_text()
# try:
#     assert info=="退出登录"
#     print("pass")
# except ValueError:
#     print("failed")
#xpath定位
result=html.xpath('//a[@class="toprighthref"]//text()')
try:
    assert result[0]=="退出登录"
    print("pass")
except ValueError:
    print("fail")

