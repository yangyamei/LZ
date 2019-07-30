import re,requests
class spider(object):
    def __init__(self):
        print("开始爬取内容")
    def getsource(self,source):
        html=requests.get(source)
        return html.text
    def changepage(self,url,total_page):
        now_page=int(re.search('pageNum=(\d+)',url,re.S).group(1))
        page_group=[]
        for i in range(now_page,total_page):
            link=re.sub('PageNum=(\d+)','pageNum=%s'%i,url,re.S)
            page_group.append(link)