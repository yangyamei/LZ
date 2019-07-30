import re
old_url='http://www.jikexueyuan.com/course/android/?pageNum=2'
total_page=20
html="""
<html lang="en">
<head>
    <title>爬虫测试</title>
</head>
<body>
<div class="topic"><a href="http://jikexueyuan.com/welcome.html">欢迎参加《听海的python3自动化接口测试》</a> 
<div class="list">
    <ul>
        <li><a href="http://jikexueyuan.com/1.html">这是第一条</a> </li>
        <li><a href="http://jikexueyuan.com/2.html">这是第2条</a> </li>
        <li><a href="http://jikexueyuan.com/3.html">这是第3条</a> </li>
    </ul>
</div>
</div>
</body>
</html>
"""
#爬取网页标题
title=re.search('<title>(.*?)</title>',html,re.S).group(1)
print(title)
#爬取链接
links=re.findall('href="(.*?)">',html)
print(links)
#爬取部分文字内容
u_text=re.findall('<ul>(.*?)</ul>',html,re.S)[0]
texts=re.findall('">(.*?)</a>',u_text,re.S)
for every_text in texts:
    print(every_text)

