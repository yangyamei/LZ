
# 导入pymysql模块
import pymysql
import pandas as pd

#state= input('state：')
# 连接database
conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")
# 得到一个可以执行SQL语句的光标对象
#cursor = conn.cursor()
# 定义要执行的SQL语句
sql = '''
select * from arc_event_repayment_order  WHERE borrow_no="jkxUJ1OH012484416796288"
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
data=collection.find_one({"optId":"reyxtdRJ1OH034167616796288"})





need_lst = ['phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion'
    , 'devId', 'serialNum', 'wifiName', 'bssid', 'electricity', 'storage', 'storageUsed', 'isCharging', 'gyroscopeX'
    , 'gyroscopeY', 'gyroscopeZ', 'isRoot']




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
                    print('mongo:{}->{}\t mysql: {}'.format(k,v,dfk))
        elif eval(v) in mydf.values:
            for dfk in mydf.columns:
                if mydf[dfk].values[0]==eval(v):
                    print('mongo:{}->{}\t mysql:{}'.format(k,v,dfk))
        else:
            print('mysql 没有'*1,k,v)
    except:
        pass