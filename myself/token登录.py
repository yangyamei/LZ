import requests
header={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
"X-Requested-With":"XMLHttpRequest",
"Connection":"keep-alive"
}
param1={"username":"xxx","password":"xxxx"}
r1=requests.post('http://xxxx/login',data=param1)
token=r1.json()["token"]
#用获取到的token模拟登录
header["token"]=token
header["Content-Length"]="9"
param2={
    "key":"value"
}
r2=requests.post('http://xxx/api/tasks',headers=header,data=param2)
print(r2.text)