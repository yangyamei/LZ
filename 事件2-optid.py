
# 导入pymysql以及pandas包模块
import pymysql
import pandas as pd

#state= input('state：')
# 连接database
conn = pymysql.connect(host="101.37.106.150",
                       user="riskc_user",
                       password="Lz@091988",
                       database="arc_lz",
                       port=3306,
                       charset="utf8")
# 得到一个可以执行SQL语句的光标对象
sql = '''
SELECT * from arc_event  where opt_id='dldcJ1VA401356116796838'
'''
# 执行SQL语句
mydf=pd.read_sql_query(sql, conn)
# 关闭光标对象
# cursor.close()
# 关闭数据库连接
conn.close()
from  pymongo  import MongoClient
client = MongoClient('172.16.157.239',6383)



db = client.admin    # mydb数据库，同上解释
db.authenticate("root", "2ICb6XyPJgdv")
collection = db.EVENT_INFO

# In[12]:
data=collection.find_one({"optId":"dldcJ1VA401356116796838"})




#必要字段检查，增加一点扩展字段
need_lst = ['phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion'
    , 'devId', 'serialNum', 'wifiName', 'bssid', 'electricity', 'storage', 'storageUsed', 'isCharging', 'gyroscopeX'
    , 'gyroscopeY', 'gyroscopeZ', 'isRoot','logMethod','logTime','isDeviceTrust','isPhoneNumTrust','authResult']




for nl in need_lst:
    if nl not in data.keys():
        print(nl)
    else:
        print('{:20}->{:>30}'.format(nl,data[nl]))


print('\n'*5)


for k,v in data.items():
    try:
        if v in mydf.values:
            for dfk in mydf.columns:
                if mydf[dfk].values[0]==v:
                    print('mongo:{}-> {}\t mysql: {}'.format(k,v,dfk))
        elif eval(v) in mydf.values:
            for dfk in mydf.columns:
                if mydf[dfk].values[0]==eval(v):
                    print('mongo:{}-> {}\t mysql:{}'.format(k,v,dfk))
        else:
            print("\033[5;31;2m%s\033[0m" % k,v)
    except:
        pass