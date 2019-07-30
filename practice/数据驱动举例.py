import requests
import xlrd
import json
from bs4 import BeautifulSoup
url='http://127.0.0.1:8090/recruit.students/login/in?'
headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
"Referer":"http://127.0.0.1:8090/recruit.students/school/manage/index"
}
payload={
    "account":"admin",
    "pwd":"660B8D2D5359FF6F94F8D3345698F88C"
}
response=requests.get(url,headers=headers,params=payload)
print(response.text)

def readExcel(rowx,filepath='C:\\Users\\linzi\\Desktop\\data.xls'):
    '''

    :param rowx: 在Excel中的行数
    :param filepath: xls文件的名称
    :return:
    '''
    book=xlrd.open_workbook(filepath)
    sheet=book.sheet_by_index(0) #通过索引获取sheet表
    return sheet.row_values(rowx) #返回第rowx行的数据
#提取第一个测试用例数据
print("第一行数据内容：",readExcel(2))
#查看数据类型
print("数据类型：{0}".format(type(readExcel(2))))
url=readExcel(2)[3]
print(url)
#从列表中提取data参数
#由于json中，标准语法中，不支持单引号，属性或者属性值，都必须是双引号括起来，用字符串方法repalace("'",'\"')
data1=readExcel(2)[4].replace("'",'\"')
print(data1)
#请求参数类型是字典，进行反序列化处理
data=json.loads(data1)
print(data)
payload=data