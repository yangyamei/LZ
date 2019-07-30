import requests
from urllib import parse

url_login='http://127.0.0.1:8090/recruit.students/login/in?account=admin&pwd=660B8D2D5359FF6F94F8D3345698F88C'
headers1={
"Connection":"keep-alive",
# "Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
# "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Referer":"http://127.0.0.1:8090/recruit.students/login/view"
}
r1=requests.get(url_login,headers=headers1)
#新建学校
url_addschool="http://127.0.0.1:8090/recruit.students/school/manage/addSchoolInfo"
headers2={
"Host":"127.0.0.1:8090",
"Connection":"keep-alive",
# "Content-Length":"85",
"Accept":"application/json, text/javascript, */*; q=0.01",
# "Origin":"http://127.0.0.1:8090",
"X-Requested-With":"XMLHttpRequest",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
"Referer":"http://127.0.0.1:8090/recruit.students/school/manage/index",
# "Accept-Encoding":"gzip, deflate, br",
# "Accept-Language":"zh-CN,zh;q=0.9",
"Cookie":"JSESSIONID=BCF38FCED7BCBA0554BF845829AA55BE; userInfoCookie="""
}
form_data={
    "schoolName":"tschool_2",
    "listSchoolType[0].id":2,
    "canRecruit":1,
    "remark":"create a new schhol_2"
}
#通过urlencode转码
form_data=parse.urlencode(form_data)
#创建session对象,可以保存cookie值
session=requests.session()
#发送携带cookie值的请求
r2=session.post(url_addschool,data=form_data,headers=headers2)
html=r2.text
print(r2.status_code)
