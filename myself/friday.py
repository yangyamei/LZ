'''
抓取贴吧内容
'''
import urllib.request
from urllib import parse
def tiebaSpider(url,beginPage,endPage):
    '''
    作用：负责处理url，分配每个url去发送请求
    :param url: 需要处理的第一个url
    :param beginPage: 执行的起始页面
    :param endPage: 执行的终止页面
    :return:
    '''
    for page in range(beginPage,endPage+1):
        pn=(page-1)*50

        filename="第"+str(page)+"页.html"
        fullurl=url+"&pn="+str(pn)
        print(fullurl)
        print(filename)
        html=loadPage(fullurl,filename)
        writeFile(html,filename)
def loadPage(url,filename):
    '''

    :param url: 需要获取的url地址
    :param filename: 处理的文件名
    :return:
    '''
    print("正在下载"+filename)
    header={
        'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                 ' (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    request=urllib.request.Request(url,headers=header)
    response=urllib.request.urlopen(request)
    return response.read()

def writeFile(html,filename):
    '''

    :param html: 服务器响应文件
    :param filename: 本地磁盘保存的文件
    :return:
    '''
    print("正在保存"+filename)
    with open(filename,'wb') as f:
        f.write(html)
    print("_"*20)
if __name__=="__main__":
    kw=input("请输入要爬取的贴吧：")
    #输入起始页和终止页，str转成int类型
    beginPage=int(input("请输入起始页："))
    endpage=int(input("请输入终止页："))
    url="http://tieba.baidu.com/f?"
    key=parse.urlencode({'kw':kw})
    url=url+key
    print(url)
    tiebaSpider(url,beginPage,endpage)
