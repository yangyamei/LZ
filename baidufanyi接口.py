import requests

# 接口的url
url = "http://fanyi.baidu.com/v2transapi"

# 接口的参数
params = {
    "from":"en",
    "to":"zh",
    "query": "test"
}

r = requests.request("post", url, params=params)

# 打印返回结果
print(r.text)