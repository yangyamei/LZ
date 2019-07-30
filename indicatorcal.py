import requests

url='http://172.16.158.55:10001/indicator/result'

payload = {
"indicatorId":"2666",
"mainAttr":"2175118",
"params": {}
}
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "49e3db42-d0cd-4361-b834-61233bca1a75"
    }
r=requests.post(url,json=payload,headers=headers)
print(r.text)