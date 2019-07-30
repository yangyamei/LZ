def zhuce(s1):
    # 导入pymysql以及pandas包模块
    import pymysql
    import pandas as pd
    #state= input('state：')
    # 连接database
    conn = pymysql.connect(host="rm-bp1c469j3h7ao1z07rw.mysql.rds.aliyuncs.com", user="app_readonly",
                           password="Linzi@9527", database="risk_biz", port=3306, charset="utf8")
    # conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")
    # 得到一个可以执行SQL语句的光标对象
    #cursor = conn.cursor()
    # 定义要执行的SQL语句
    sql = '''
    SELECT * from arc_event  where opt_id='%s'
    '''%s1
    # 执行SQL语句
    mydf=pd.read_sql_query(sql, conn)
    # 关闭光标对象
    # cursor.close()
    # 关闭数据库连接
    conn.close()
    from  pymongo  import MongoClient
    # client = MongoClient('172.16.157.239',6383)
    client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)
    db = client.admin    # mydb数据库，同上解释
    # db.authenticate("root", "2ICb6XyPJgdv")
    db.authenticate("root", "c4N3pVMN8zfBwhOC")
    collection = db.EVENT_INFO
    # In[12]:
    data=collection.find_one({"optId":s1})
    #必要字段检查，增加一点扩展字段
    need_lst = ['eventBeginTime','codeValidResult','authResult',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion'
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
                        print('mongo:{}-> {}\t mysql: {}'.format(k,v,dfk))
            elif eval(v) in mydf.values:
                for dfk in mydf.columns:
                    if mydf[dfk].values[0]==eval(v):
                        print('mongo:{}-> {}\t mysql:{}'.format(k,v,dfk))
            else:
                print("\033[5;31;2m%s\033[0m" % k,v)
        except:
            pass


def Acard(s1):
    # 导入pymysql以及pandas包模块
    import pymysql
    import pandas as pd
    #state= input('state：')
    # 连接database
    conn = pymysql.connect(host="rm-bp1c469j3h7ao1z07rw.mysql.rds.aliyuncs.com", user="app_readonly",
                           password="Linzi@9527", database="risk_biz", port=3306, charset="utf8")
    # conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")
    # 得到一个可以执行SQL语句的光标对象
    #cursor = conn.cursor()
    # 定义要执行的SQL语句
    sql = '''
    SELECT * from arc_event  where opt_id='%s'
    '''%s1
    # 执行SQL语句
    mydf=pd.read_sql_query(sql, conn)
    # 关闭光标对象
    # cursor.close()
    # 关闭数据库连接
    conn.close()
    from  pymongo  import MongoClient
    # client = MongoClient('172.16.157.239',6383)
    client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)
    db = client.admin    # mydb数据库，同上解释
    # db.authenticate("root", "2ICb6XyPJgdv")
    db.authenticate("root", "c4N3pVMN8zfBwhOC")
    collection = db.EVENT_INFO
    # In[12]:
    data=collection.find_one({"optId":s1})
    #必要字段检查，增加一点扩展字段
    need_lst = ['checkResult','tokenId','blackBox','cardNo','devType','ipAddress','appName','checkTime',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion'
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
                        print('mongo:{}-> {}\t mysql: {}'.format(k,v,dfk))
            elif eval(v) in mydf.values:
                for dfk in mydf.columns:
                    if mydf[dfk].values[0]==eval(v):
                        print('mongo:{}-> {}\t mysql:{}'.format(k,v,dfk))
            else:
                print("\033[5;31;2m%s\033[0m" % k,v)
        except:
            pass


def Bcard(s1):
    # 导入pymysql以及pandas包模块
    import pymysql
    import pandas as pd

    #state= input('state：')
    # 连接database
    conn = pymysql.connect(host="rm-bp1c469j3h7ao1z07rw.mysql.rds.aliyuncs.com", user="app_readonly",
                           password="Linzi@9527", database="risk_biz", port=3306, charset="utf8")
    # conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")
    # 得到一个可以执行SQL语句的光标对象
    #cursor = conn.cursor()
    # 定义要执行的SQL语句

    sql = '''
    SELECT * from arc_event  where opt_id='%s'
    '''%s1
    # 执行SQL语句
    mydf=pd.read_sql_query(sql, conn)
    # 关闭光标对象
    # cursor.close()
    # 关闭数据库连接
    conn.close()
    from  pymongo  import MongoClient
    client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)
    # client = MongoClient('172.16.157.239', 6383)
    #client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)
    db = client.admin    # mydb数据库，同上解释
    # db.authenticate("root", "2ICb6XyPJgdv")
    db.authenticate("root", "c4N3pVMN8zfBwhOC")
    collection = db.EVENT_INFO
    # In[12]:
    data=collection.find_one({"optId":s1})
    #必要字段检查，增加一点扩展字段
    need_lst = ['checkTime', 'checkResult', 'time', 'poundage', 'realAmount', 'orderAmount', 'nper', 'inLoanOverdueDay','isCycleBorrow','orderNo',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion'
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
                        print('mongo:{}-> {}\t mysql: {}'.format(k,v,dfk))
            elif eval(v) in mydf.values:
                for dfk in mydf.columns:
                    if mydf[dfk].values[0]==eval(v):
                        print('mongo:{}-> {}\t mysql:{}'.format(k,v,dfk))
            else:
                print("\033[5;31;2m%s\033[0m" % k,v)
        except:
            pass
def Borrowingevent(s1):
    # 导入pymysql以及pandas包模块
    import pymysql
    import pandas as pd
    #state= input('state：')
    # 连接database
    # conn = pymysql.connect(host="101.37.106.150", user="riskc_user", password="Lz@091988", database="arc_lz", port=3306,charset="utf8")
    conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")
    # 得到一个可以执行SQL语句的光标对象
    #cursor = conn.cursor()
    # 定义要执行的SQL语句
    sql = '''
    SELECT * from arc_event  where opt_id='%s'
    '''%s1
    # 执行SQL语句
    mydf=pd.read_sql_query(sql, conn)
    # 关闭光标对象
    # cursor.close()
    # 关闭数据库连接
    conn.close()
    from  pymongo  import MongoClient
    # client = MongoClient('172.16.157.239', 6383)
    client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)
    db = client.admin    # mydb数据库，同上解释
    # db.authenticate("root", "2ICb6XyPJgdv")
    db.authenticate("root", "c4N3pVMN8zfBwhOC")
    collection = db.EVENT_INFO
    # In[12]:
    data=collection.find_one({"optId":s1})
    #必要字段检查，增加一点扩展字段
    need_lst = ['borrowNo', 'usedAmount', 'availableAmount', 'creditAmount', 'borrowCash', 'borrowTime', 'payCashTime', 'maxRepaymentTime', 'installmentCnt', 'installmentBill','borrowStatus',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion'
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
                        print('mongo:{}-> {}\t mysql: {}'.format(k,v,dfk))
            elif eval(v) in mydf.values:
                for dfk in mydf.columns:
                    if mydf[dfk].values[0]==eval(v):
                        print('mongo:{}-> {}\t mysql:{}'.format(k,v,dfk))
            else:
                print("\033[5;31;2m%s\033[0m" % k,v)
        except:
            pass
# Borrowingevent('bsqbblRJ4HJ5844732100005')

def Carriercertificationevent(s1):
    # 导入pymysql以及pandas包模块
    import pymysql
    import pandas as pd
    #state= input('state：')
    # 连接database
    conn = pymysql.connect(host="rm-bp1c469j3h7ao1z07rw.mysql.rds.aliyuncs.com", user="app_readonly",
                           password="Linzi@9527", database="risk_biz", port=3306, charset="utf8")
    #conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")
    # 得到一个可以执行SQL语句的光标对象
    #cursor = conn.cursor()
    # 定义要执行的SQL语句
    sql = '''
    SELECT * from arc_event  where opt_id='%s'
    '''%s1
    # 执行SQL语句
    mydf=pd.read_sql_query(sql, conn)
    # 关闭光标对象
    # cursor.close()
    # 关闭数据库连接
    conn.close()
    from  pymongo  import MongoClient
    client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)
    # client = MongoClient('172.16.157.239', 6383)
    db = client.admin    # mydb数据库，同上解释
    db.authenticate("root", "c4N3pVMN8zfBwhOC")
    # db.authenticate("root", "2ICb6XyPJgdv")
    collection = db.EVENT_INFO
    # In[12]:
    data=collection.find_one({"optId":s1})
    #必要字段检查，增加一点扩展字段
    need_lst = ['eventBeginTime',
                'eventEndTime',
                'codeValidResult',
                'authResult',

                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion'
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
                        print('mongo:{}-> {}\t mysql: {}'.format(k,v,dfk))
            elif eval(v) in mydf.values:
                for dfk in mydf.columns:
                    if mydf[dfk].values[0]==eval(v):
                        print('mongo:{}-> {}\t mysql:{}'.format(k,v,dfk))
            else:
                print("\033[5;31;2m%s\033[0m" % k,v)
        except:
            pass
#s1='refxblRJ3QH263261518972220'
def Faceverificationevent(s1):
    # 导入pymysql以及pandas包模块
    import pymysql
    import pandas as pd
    #state= input('state：')
    # 连接database
    conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")
    #conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")
    # 得到一个可以执行SQL语句的光标对象
    #cursor = conn.cursor()
    # 定义要执行的SQL语句
    sql = '''
    SELECT * from arc_event  where opt_id='%s'
    '''%s1
    # 执行SQL语句
    mydf=pd.read_sql_query(sql, conn)
    # 关闭光标对象
    # cursor.close()
    # 关闭数据库连接
    conn.close()
    from  pymongo  import MongoClient
    client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)
    db = client.admin    # mydb数据库，同上解释
    db.authenticate("root", "c4N3pVMN8zfBwhOC")
    collection = db.EVENT_INFO
    # In[12]:
    data=collection.find_one({"optId":s1})
    #必要字段检查，增加一点扩展字段
    need_lst = ['eventBeginTime',
                'eventEndTime',
                'faceReplaced',
                'authResult',
                'confidence',
                'liveness',
                'syntheticFaceConfidence',
                'maskConfidence',
                'screenReplayConfidence',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion'
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
                        print('mongo:{}-> {}\t mysql: {}'.format(k,v,dfk))
            elif eval(v) in mydf.values:
                for dfk in mydf.columns:
                    if mydf[dfk].values[0]==eval(v):
                        print('mongo:{}-> {}\t mysql:{}'.format(k,v,dfk))
            else:
                print("\033[5;31;2m%s\033[0m" % k,v)
        except:
            pass


def Liftingamount(s1):

    # 导入pymysql以及pandas包模块
    import pymysql
    import pandas as pd

    #state= input('state：')
    # 连接database
    # conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")
    conn = pymysql.connect(host="rm-bp1c469j3h7ao1z07rw.mysql.rds.aliyuncs.com", user="app_readonly",
    password="Linzi@9527", database="risk_biz", port=3306, charset="utf8")

    # 得到一个可以执行SQL语句的光标对象
    #cursor = conn.cursor()
    # 定义要执行的SQL语句

    sql = '''
    SELECT * from arc_event  where opt_id='%s'
    '''%s1

    # 执行SQL语句
    mydf=pd.read_sql_query(sql, conn)

    # 关闭光标对象
    # cursor.close()
    # 关闭数据库连接
    conn.close()

    from  pymongo  import MongoClient

    # client = MongoClient('172.16.157.239', 6383)
    client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)


    db = client.admin    # mydb数据库，同上解释

    # db.authenticate("root", "2ICb6XyPJgdv")
    db.authenticate("root", "c4N3pVMN8zfBwhOC")
    collection = db.EVENT_INFO

    # In[12]:
    data=collection.find_one({"optId":s1})




    #必要字段检查，增加一点扩展字段

    need_lst = ['borrowNo','amount', 'maxOverdueDays','installmentCnt','billMaxOverdueDay','billMinOverdueDay','billNo','income',
                'billIncome','isSettle','overdueDays', 'overdueCount',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion'
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
                        print('mongo:{}-> {}\t mysql: {}'.format(k,v,dfk))
            elif eval(v) in mydf.values:
                for dfk in mydf.columns:
                    if mydf[dfk].values[0]==eval(v):
                        print('mongo:{}-> {}\t mysql:{}'.format(k,v,dfk))
            else:
                print("\033[5;31;2m%s\033[0m" % k,v)
        except:
            pass


def Offlinerepayment(s1):

    # 导入pymysql以及pandas包模块
    import pymysql
    import pandas as pd

    #state= input('state：')
    # 连接database
    conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")
    #conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")

    # 得到一个可以执行SQL语句的光标对象
    #cursor = conn.cursor()
    # 定义要执行的SQL语句

    sql = '''
    SELECT * from arc_event  where opt_id='%s'
    '''

    # 执行SQL语句
    mydf=pd.read_sql_query(sql, conn)

    # 关闭光标对象
    # cursor.close()
    # 关闭数据库连接
    conn.close()

    from  pymongo  import MongoClient



    client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)
    # client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)


    db = client.admin    # mydb数据库，同上解释
    db.authenticate("root", "c4N3pVMN8zfBwhOC")
    # db.authenticate("root", "c4N3pVMN8zfBwhOC")
    collection = db.EVENT_INFO

    # In[12]:
    data=collection.find_one({"optId":s1})




    #必要字段检查，增加一点扩展字段

    need_lst = ['borrowNo', 'borrowAmount', 'borrowType', 'amount', 'isPayOff', 'installmentCnt', 'installmentNo', 'repaymentType', 'repaymentNo', 'repaymentStatus', 'repaymentAmount', 'actualPaymentAmount', 'repaymentFailReason', 'discountId', 'discountName', 'income', 'interest', 'overdueAmount', 'overdueDay', 'availableAmount', 'discountPrice', 'maxRepaymentTime',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion'
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
                        print('mongo:{}-> {}\t mysql: {}'.format(k,v,dfk))
            elif eval(v) in mydf.values:
                for dfk in mydf.columns:
                    if mydf[dfk].values[0]==eval(v):
                        print('mongo:{}-> {}\t mysql:{}'.format(k,v,dfk))
            else:
                print("\033[5;31;2m%s\033[0m" % k,v)
        except:
            pass

def Realnamecertificationevent(s1):
    # 导入pymysql以及pandas包模块
    import pymysql
    import pandas as pd

    #state= input('state：')
    # 连接database
    conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")
    #conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")
    # 得到一个可以执行SQL语句的光标对象
    #cursor = conn.cursor()
    # 定义要执行的SQL语句

    sql = '''
    SELECT * from arc_event  where opt_id='%s'
    '''%s1

    # 执行SQL语句
    mydf=pd.read_sql_query(sql, conn)

    # 关闭光标对象
    # cursor.close()
    # 关闭数据库连接
    conn.close()

    from  pymongo  import MongoClient
    client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)
    # client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)
    db = client.admin    # mydb数据库，同上解释
    db.authenticate("root", "c4N3pVMN8zfBwhOC")
    # db.authenticate("root", "c4N3pVMN8zfBwhOC")
    collection = db.EVENT_INFO

    # In[12]:
    data=collection.find_one({"optId":s1})




    #必要字段检查，增加一点扩展字段
    need_lst = ['realName',
                'idCardNo',
                'phoneNum',
                'eventBeginTime',
                'validateChannel',
                'eventEndTime',


                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion'
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
                        print('mongo:{}-> {}\t mysql: {}'.format(k,v,dfk))
            elif eval(v) in mydf.values:
                for dfk in mydf.columns:
                    if mydf[dfk].values[0]==eval(v):
                        print('mongo:{}-> {}\t mysql:{}'.format(k,v,dfk))
            else:
                print("\033[5;31;2m%s\033[0m" % k,v)
        except:
            pass

def Registrationoperation(s1):
    # 导入pymysql以及pandas包模块
    import pymysql
    import pandas as pd

    #state= input('state：')
    # 连接database
    conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")
    #conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")
    # 得到一个可以执行SQL语句的光标对象
    #cursor = conn.cursor()
    # 定义要执行的SQL语句

    sql = '''
    SELECT * from arc_event  where opt_id='%s'
    '''%s1

    # 执行SQL语句
    mydf=pd.read_sql_query(sql, conn)

    # 关闭光标对象
    # cursor.close()
    # 关闭数据库连接
    conn.close()

    from  pymongo  import MongoClient
    client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)



    db = client.admin    # mydb数据库，同上解释
    db.authenticate("root", "c4N3pVMN8zfBwhOC")
    collection = db.EVENT_INFO

    # In[12]:
    data=collection.find_one({"optId":s1})




    #必要字段检查，增加一点扩展字段
    need_lst = ['phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion'
        , 'devId', 'serialNum', 'wifiName', 'bssid', 'electricity', 'storage', 'storageUsed', 'isCharging', 'gyroscopeX'
        , 'gyroscopeY', 'gyroscopeZ', 'isRoot',
        'eventBeginTime', 'codeValidResult', 'authResult']



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

def Repaymentevent(s1):
    # 导入pymysql以及pandas包模块
    import pymysql
    import pandas as pd

    #state= input('state：')
    # 连接database
    conn = pymysql.connect(host="101.37.106.150", user="riskc_user", password="Lz@091988", database="arc_lz", port=3306,charset="utf8")
    #conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")

    # 得到一个可以执行SQL语句的光标对象
    #cursor = conn.cursor()
    # 定义要执行的SQL语句

    sql = '''
    SELECT * from arc_event  where opt_id='%s'
    '''%s1

    # 执行SQL语句
    mydf=pd.read_sql_query(sql, conn)

    # 关闭光标对象
    # cursor.close()
    # 关闭数据库连接
    conn.close()

    from  pymongo  import MongoClient

    client = MongoClient('172.16.157.239', 6383)
    #client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)


    db = client.admin    # mydb数据库，同上解释

    db.authenticate("root", "2ICb6XyPJgdv")

    #db.authenticate("root", "c4N3pVMN8zfBwhOC")
    collection = db.EVENT_INFO

    # In[12]:
    data=collection.find_one({"optId":s1})




    #必要字段检查，增加一点扩展字段

    need_lst = ['borrowNo', 'borrowAmount', 'borrowType', 'amount','isAllPayOff','isPayOff', 'installmentCnt', 'installmentNo',
                'repaymentType', 'repaymentNo', 'repaymentStatus', 'repaymentAmount', 'actualPaymentAmount', 'repaymentFailReason',
                'discountId', 'discountName', 'income', 'interest', 'overdueAmount', 'overdueDay', 'availableAmount', 'discountPrice', 'maxRepaymentTime',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion'
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
                        print('mongo:{}-> {}\t mysql: {}'.format(k,v,dfk))
            elif eval(v) in mydf.values:
                for dfk in mydf.columns:
                    if mydf[dfk].values[0]==eval(v):
                        print('mongo:{}-> {}\t mysql:{}'.format(k,v,dfk))
            else:
                print("\033[5;31;2m%s\033[0m" % k,v)
        except:
            pass



def Advancecredit(s1):
    # 导入pymysql以及pandas包模块
    import pymysql
    import pandas as pd

    #state= input('state：')
    # 连接database
    conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")
    #conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")

    # 得到一个可以执行SQL语句的光标对象
    #cursor = conn.cursor()
    # 定义要执行的SQL语句

    sql = '''
    SELECT * from arc_event  where opt_id='%s'
    '''%s1

    # 执行SQL语句
    mydf=pd.read_sql_query(sql, conn)

    # 关闭光标对象
    # cursor.close()
    # 关闭数据库连接
    conn.close()

    from  pymongo  import MongoClient

    client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)
    #client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)


    db = client.admin    # mydb数据库，同上解释

    db.authenticate("root", "c4N3pVMN8zfBwhOC")

    #db.authenticate("root", "c4N3pVMN8zfBwhOC")
    collection = db.EVENT_INFO

    # In[12]:
    data=collection.find_one({"optId":s1})




    #必要字段检查，增加一点扩展字段

    need_lst = ['checkResult','checkTime',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion'
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
                        print('mongo:{}-> {}\t mysql: {}'.format(k,v,dfk))
            elif eval(v) in mydf.values:
                for dfk in mydf.columns:
                    if mydf[dfk].values[0]==eval(v):
                        print('mongo:{}-> {}\t mysql:{}'.format(k,v,dfk))
            else:
                print("\033[5;31;2m%s\033[0m" % k,v)
        except:
            pass



def Loginsynchronizationevent(s1):
    # 导入pymysql以及pandas包模块
    import pymysql
    import pandas as pd

    #state= input('state：')
    # 连接database
    # conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")
    conn = pymysql.connect(host="rm-bp1c469j3h7ao1z07rw.mysql.rds.aliyuncs.com", user="app_readonly",
                           password="Linzi@9527", database="risk_biz", port=3306, charset="utf8")
    #conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")

    # 得到一个可以执行SQL语句的光标对象
    #cursor = conn.cursor()
    # 定义要执行的SQL语句

    sql = '''
    SELECT * from arc_event  where opt_id='%s'
    '''%s1

    # 执行SQL语句
    mydf=pd.read_sql_query(sql, conn)

    # 关闭光标对象
    # cursor.close()
    # 关闭数据库连接
    conn.close()

    from  pymongo  import MongoClient

    # client = MongoClient('172.16.157.239', 6383)
    client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)


    db = client.admin    # mydb数据库，同上解释

    # db.authenticate("root", "2ICb6XyPJgdv")
    db.authenticate("root", "c4N3pVMN8zfBwhOC")
    collection = db.EVENT_INFO

    # In[12]:
    data=collection.find_one({"optId":s1})




    #必要字段检查，增加一点扩展字段

    need_lst = ['isDeviceTrust','isPhoneNumTrust',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion'
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
                        print('mongo:{}-> {}\t mysql: {}'.format(k,v,dfk))
            elif eval(v) in mydf.values:
                for dfk in mydf.columns:
                    if mydf[dfk].values[0]==eval(v):
                        print('mongo:{}-> {}\t mysql:{}'.format(k,v,dfk))
            else:
                print("\033[5;31;2m%s\033[0m" % k,v)
        except:
            pass





def Logintoanasynchronousevent(s1):
    # 导入pymysql以及pandas包模块
    import pymysql
    import pandas as pd

    #state= input('state：')
    # 连接database
    conn = pymysql.connect(host="rm-bp1c469j3h7ao1z07rw.mysql.rds.aliyuncs.com", user="app_readonly",
                           password="Linzi@9527", database="risk_biz", port=3306, charset="utf8")
    #conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")

    # 得到一个可以执行SQL语句的光标对象
    #cursor = conn.cursor()
    # 定义要执行的SQL语句

    sql = '''
    SELECT * from arc_event  where opt_id='%s'
    '''%s1

    # 执行SQL语句
    mydf=pd.read_sql_query(sql, conn)

    # 关闭光标对象
    # cursor.close()
    # 关闭数据库连接
    conn.close()

    from  pymongo  import MongoClient

    # client = MongoClient('172.16.157.239', 6383)
    client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)


    db = client.admin    # mydb数据库，同上解释

    # db.authenticate("root", "2ICb6XyPJgdv")
    db.authenticate("root", "c4N3pVMN8zfBwhOC")
    collection = db.EVENT_INFO

    # In[12]:
    data=collection.find_one({"optId":s1})




    #必要字段检查，增加一点扩展字段

    need_lst = ['logMethod', 'logTime', 'isDeviceTrust', 'isPhoneNumTrust', 'authResult',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion'
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
                        print('mongo:{}-> {}\t mysql: {}'.format(k,v,dfk))
            elif eval(v) in mydf.values:
                for dfk in mydf.columns:
                    if mydf[dfk].values[0]==eval(v):
                        print('mongo:{}-> {}\t mysql:{}'.format(k,v,dfk))
            else:
                print("\033[5;31;2m%s\033[0m" % k,v)
        except:
            pass





def SMSevent(s1):
    # 导入pymysql以及pandas包模块
    import pymysql
    import pandas as pd

    #state= input('state：')
    # 连接database
    conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")
    #conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")

    # 得到一个可以执行SQL语句的光标对象
    #cursor = conn.cursor()
    # 定义要执行的SQL语句

    sql = '''
    SELECT * from arc_event  where opt_id='%s'
    '''%s1

    # 执行SQL语句
    mydf=pd.read_sql_query(sql, conn)

    # 关闭光标对象
    # cursor.close()
    # 关闭数据库连接
    conn.close()

    from  pymongo  import MongoClient

    client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)
    #client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)


    db = client.admin    # mydb数据库，同上解释

    db.authenticate("root", "c4N3pVMN8zfBwhOC")

    #db.authenticate("root", "c4N3pVMN8zfBwhOC")
    collection = db.EVENT_INFO

    # In[12]:
    data=collection.find_one({"optId":s1})




    #必要字段检查，增加一点扩展字段

    need_lst = [ 'codeValidType', 'codeSendTime', 'isSend',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion'
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
                        print('mongo:{}-> {}\t mysql: {}'.format(k,v,dfk))
            elif eval(v) in mydf.values:
                for dfk in mydf.columns:
                    if mydf[dfk].values[0]==eval(v):
                        print('mongo:{}-> {}\t mysql:{}'.format(k,v,dfk))
            else:
                print("\033[5;31;2m%s\033[0m" % k,v)
        except:
            pass


def tiedcardcertification(s1):
    # 导入pymysql以及pandas包模块
    import pymysql
    import pandas as pd

    #state= input('state：')
    # 连接database
    conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")
    #conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")

    # 得到一个可以执行SQL语句的光标对象
    #cursor = conn.cursor()
    # 定义要执行的SQL语句

    sql = '''
    SELECT * from arc_event  where opt_id='%s'
    '''%s1

    # 执行SQL语句
    mydf=pd.read_sql_query(sql, conn)

    # 关闭光标对象
    # cursor.close()
    # 关闭数据库连接
    conn.close()

    from  pymongo  import MongoClient

    client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)
    #client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)


    db = client.admin    # mydb数据库，同上解释

    db.authenticate("root", "c4N3pVMN8zfBwhOC")

    #db.authenticate("root", "c4N3pVMN8zfBwhOC")
    collection = db.EVENT_INFO

    # In[12]:
    data=collection.find_one({"optId":s1})




    #必要字段检查，增加一点扩展字段

    need_lst = [ 'eventBeginTime', 'eventEndTime', 'phoneInputContent', 'inputBankCard', 'accountBank', 'codeValidResult', 'authResult',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion'
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
                        print('mongo:{}-> {}\t mysql: {}'.format(k,v,dfk))
            elif eval(v) in mydf.values:
                for dfk in mydf.columns:
                    if mydf[dfk].values[0]==eval(v):
                        print('mongo:{}-> {}\t mysql:{}'.format(k,v,dfk))
            else:
                print("\033[5;31;2m%s\033[0m" % k,v)
        except:
            pass
'''
身份认证
'''
def identityauthentication(s1):
    # 导入pymysql以及pandas包模块
    import pymysql
    import pandas as pd

    #state= input('state：')
    # 连接database
    conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")
    #conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")

    # 得到一个可以执行SQL语句的光标对象
    #cursor = conn.cursor()
    # 定义要执行的SQL语句

    sql = '''
    SELECT * from arc_event  where opt_id='%s'
    '''%s1

    # 执行SQL语句
    mydf=pd.read_sql_query(sql, conn)

    # 关闭光标对象
    # cursor.close()
    # 关闭数据库连接
    conn.close()

    from  pymongo  import MongoClient

    client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)
    #client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)


    db = client.admin    # mydb数据库，同上解释

    db.authenticate("root", "c4N3pVMN8zfBwhOC")

    #db.authenticate("root", "c4N3pVMN8zfBwhOC")
    collection = db.EVENT_INFO

    # In[12]:
    data=collection.find_one({"optId":s1})




    #必要字段检查，增加一点扩展字段

    need_lst = [ 'name', 'idCardNo', 'isScanIdCard', 'idCardAddress', 'idCardNation', 'idCardCreateTime', 'idCardEndTime', 'idCardBirtherDay',
                 'idCardIssuanceAuthority', 'idCardFrontPhoto', 'idCardOppositePhoto', 'eventBeginTime', 'eventEndTime',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion'
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
                        print('mongo:{}-> {}\t mysql: {}'.format(k,v,dfk))
            elif eval(v) in mydf.values:
                for dfk in mydf.columns:
                    if mydf[dfk].values[0]==eval(v):
                        print('mongo:{}-> {}\t mysql:{}'.format(k,v,dfk))
            else:
                print("\033[5;31;2m%s\033[0m" % k,v)
        except:
            pass


'''
修改登录密码
'''
def Modifytheloginpassword(s1):
    # 导入pymysql以及pandas包模块
    import pymysql
    import pandas as pd

    #state= input('state：')
    # 连接database
    conn = pymysql.connect(host="rm-bp1c469j3h7ao1z07rw.mysql.rds.aliyuncs.com", user="app_readonly",
                           password="Linzi@9527", database="risk_biz", port=3306, charset="utf8")
    #conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")

    # 得到一个可以执行SQL语句的光标对象
    #cursor = conn.cursor()
    # 定义要执行的SQL语句

    sql = '''
    SELECT * from arc_event  where opt_id='%s'
    '''%s1

    # 执行SQL语句
    mydf=pd.read_sql_query(sql, conn)

    # 关闭光标对象
    # cursor.close()
    # 关闭数据库连接
    conn.close()

    from  pymongo  import MongoClient

    # client = MongoClient('172.16.157.239', 6383)
    client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)


    db = client.admin    # mydb数据库，同上解释

    # db.authenticate("root", "2ICb6XyPJgdv")
    db.authenticate("root", "c4N3pVMN8zfBwhOC")
    collection = db.EVENT_INFO

    # In[12]:
    data=collection.find_one({"optId":s1})




    #必要字段检查，增加一点扩展字段

    need_lst = ['validMethod', 'eventBeginTime', 'oldLogPasswordTime', 'newLogPasswordTime', 'eventEndTime', 'authResult',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion'
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
                        print('mongo:{}-> {}\t mysql: {}'.format(k,v,dfk))
            elif eval(v) in mydf.values:
                for dfk in mydf.columns:
                    if mydf[dfk].values[0]==eval(v):
                        print('mongo:{}-> {}\t mysql:{}'.format(k,v,dfk))
            else:
                print("\033[5;31;2m%s\033[0m" % k,v)
        except:
            pass
'''找回登录密码'''
def Findloginpassword(s1):
    # 导入pymysql以及pandas包模块
    import pymysql
    import pandas as pd

    #state= input('state：')
    # 连接database
    conn = pymysql.connect(host="rm-bp1c469j3h7ao1z07rw.mysql.rds.aliyuncs.com", user="app_readonly",
                           password="Linzi@9527", database="risk_biz", port=3306, charset="utf8")
    #conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")

    # 得到一个可以执行SQL语句的光标对象
    #cursor = conn.cursor()
    # 定义要执行的SQL语句

    sql = '''
    SELECT * from arc_event  where opt_id='%s'
    '''%s1

    # 执行SQL语句
    mydf=pd.read_sql_query(sql, conn)

    # 关闭光标对象
    # cursor.close()
    # 关闭数据库连接
    conn.close()

    from  pymongo  import MongoClient

    # client = MongoClient('172.16.157.239', 6383)
    client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)


    db = client.admin    # mydb数据库，同上解释

    # db.authenticate("root", "2ICb6XyPJgdv")
    db.authenticate("root", "c4N3pVMN8zfBwhOC")
    collection = db.EVENT_INFO

    # In[12]:
    data=collection.find_one({"optId":s1})




    #必要字段检查，增加一点扩展字段

    need_lst = ['validMethod', 'codeValidResult', 'eventBeginTime', 'phoneInputTime', 'phoneInputContent', 'newLogPasswordTime','eventEndTime','authResult',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion'
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
                        print('mongo:{}-> {}\t mysql: {}'.format(k,v,dfk))
            elif eval(v) in mydf.values:
                for dfk in mydf.columns:
                    if mydf[dfk].values[0]==eval(v):
                        print('mongo:{}-> {}\t mysql:{}'.format(k,v,dfk))
            else:
                print("\033[5;31;2m%s\033[0m" % k,v)
        except:
            pass



'''修改支付密码'''
def ModifythePayinpassword(s1):
    # 导入pymysql以及pandas包模块
    import pymysql
    import pandas as pd

    #state= input('state：')
    # 连接database
    conn = pymysql.connect(host="rm-bp1c469j3h7ao1z07rw.mysql.rds.aliyuncs.com", user="app_readonly",
                           password="Linzi@9527", database="risk_biz", port=3306, charset="utf8")
    #conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")

    # 得到一个可以执行SQL语句的光标对象
    #cursor = conn.cursor()
    # 定义要执行的SQL语句

    sql = '''
    SELECT * from arc_event  where opt_id='%s'
    '''%s1

    # 执行SQL语句
    mydf=pd.read_sql_query(sql, conn)

    # 关闭光标对象
    # cursor.close()
    # 关闭数据库连接
    conn.close()

    from  pymongo  import MongoClient
    # client = MongoClient('172.16.157.239', 6383)
    client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)


    db = client.admin    # mydb数据库，同上解释

    # db.authenticate("root", "2ICb6XyPJgdv")
    db.authenticate("root", "c4N3pVMN8zfBwhOC")
    collection = db.EVENT_INFO

    # In[12]:
    data=collection.find_one({"optId":s1})




    #必要字段检查，增加一点扩展字段

    need_lst = ['validMethod', 'eventBeginTime', 'oldPayPasswordTime', 'newPayPasswordTime', 'validEndTime','codeValidResult', 'authResult',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion'
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
                        print('mongo:{}-> {}\t mysql: {}'.format(k,v,dfk))
            elif eval(v) in mydf.values:
                for dfk in mydf.columns:
                    if mydf[dfk].values[0]==eval(v):
                        print('mongo:{}-> {}\t mysql:{}'.format(k,v,dfk))
            else:
                print("\033[5;31;2m%s\033[0m" % k,v)
        except:
            pass
'''
通讯录
'''
def PhoneBook(s1):
    # 导入pymysql以及pandas包模块
    import pymysql
    import pandas as pd

    #state= input('state：')
    # 连接database
    conn = pymysql.connect(host="rm-bp1c469j3h7ao1z07rw.mysql.rds.aliyuncs.com", user="app_readonly",
                           password="Linzi@9527", database="risk_biz", port=3306, charset="utf8")
    #conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")

    # 得到一个可以执行SQL语句的光标对象
    #cursor = conn.cursor()
    # 定义要执行的SQL语句

    sql = '''
    SELECT * from arc_event  where opt_id='%s'
    '''%s1

    # 执行SQL语句
    mydf=pd.read_sql_query(sql, conn)

    # 关闭光标对象
    # cursor.close()
    # 关闭数据库连接
    conn.close()

    from  pymongo  import MongoClient

    client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)
    #client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)


    db = client.admin    # mydb数据库，同上解释

    db.authenticate("root", "c4N3pVMN8zfBwhOC")

    #db.authenticate("root", "c4N3pVMN8zfBwhOC")
    collection = db.EVENT_INFO

    # In[12]:
    data=collection.find_one({"optId":s1})




    #必要字段检查，增加一点扩展字段

    need_lst = ['eventBeginTime', 'eventEndTime', 'authResult',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion'
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
                        print('mongo:{}-> {}\t mysql: {}'.format(k,v,dfk))
            elif eval(v) in mydf.values:
                for dfk in mydf.columns:
                    if mydf[dfk].values[0]==eval(v):
                        print('mongo:{}-> {}\t mysql:{}'.format(k,v,dfk))
            else:
                print("\033[5;31;2m%s\033[0m" % k,v)
        except:
            pass

'''
预风控事件
'''
def PreControl(s1):
    # 导入pymysql以及pandas包模块
    import pymysql
    import pandas as pd

    #state= input('state：')
    # 连接database
    conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")
    #conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")

    # 得到一个可以执行SQL语句的光标对象
    #cursor = conn.cursor()
    # 定义要执行的SQL语句

    sql = '''
    SELECT * from arc_event  where opt_id='%s'
    '''%s1

    # 执行SQL语句
    mydf=pd.read_sql_query(sql, conn)

    # 关闭光标对象
    # cursor.close()
    # 关闭数据库连接
    conn.close()

    from  pymongo  import MongoClient

    client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)
    #client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)


    db = client.admin    # mydb数据库，同上解释

    db.authenticate("root", "c4N3pVMN8zfBwhOC")

    #db.authenticate("root", "c4N3pVMN8zfBwhOC")
    collection = db.EVENT_INFO

    # In[12]:
    data=collection.find_one({"optId":s1})




    #必要字段检查，增加一点扩展字段

    need_lst = ['checkTime', 'checkResult',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion'
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
                        print('mongo:{}-> {}\t mysql: {}'.format(k,v,dfk))
            elif eval(v) in mydf.values:
                for dfk in mydf.columns:
                    if mydf[dfk].values[0]==eval(v):
                        print('mongo:{}-> {}\t mysql:{}'.format(k,v,dfk))
            else:
                print("\033[5;31;2m%s\033[0m" % k,v)
        except:
            pass
'''
紧急联系人事件,该事件无环境字段,有多条数据
'''
def EmergencyContact(s1):
    # 导入pymysql以及pandas包模块
    import pymysql
    import pandas as pd

    #state= input('state：')
    # 连接database
    # conn = pymysql.connect(host="101.37.106.150", user="riskc_user", password="Lz@091988", database="arc_lz", port=3306,charset="utf8")
    conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")

    # 得到一个可以执行SQL语句的光标对象
    #cursor = conn.cursor()
    # 定义要执行的SQL语句

    sql = '''
    SELECT * from arc_event  where opt_id='%s'
    '''%s1

    # 执行SQL语句
    mydf=pd.read_sql_query(sql, conn)

    # 关闭光标对象
    # cursor.close()
    # 关闭数据库连接
    conn.close()

    from  pymongo  import MongoClient

    # client = MongoClient('172.16.157.239', 6383)
    client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)
    db = client.admin    # mydb数据库，同上解释
    # db.authenticate("root", "2ICb6XyPJgdv")
    db.authenticate("root", "c4N3pVMN8zfBwhOC")
    collection = db.EVENT_INFO

    # In[12]:
    data_list=collection.find({"optId":s1}) #返回列表
    #必要字段检查，增加一点扩展字段
    # for data in data_list:
    #     return data

    need_lst = ['relation', 'name','phone','idNo','houseAddress','company','workAddress','relation_channel']
    for data in data_list:
        for nl in need_lst:
            if nl not in data.keys():
                print(nl)
            else:
                print('{:20}->{:>30}'.format(nl,data[nl]))
        print('下一条****************************************\n')


    print('\n'*5)



    for data in data_list:
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
'''预授信'''
'''
预授信事件
'''
def pre_approval(s1):
    # 导入pymysql以及pandas包模块
    import pymysql
    import pandas as pd

    #state= input('state：')
    # 连接database
    # conn = pymysql.connect(host="101.37.106.150", user="riskc_user",password="Lz@091988",database="arc_lz",port=3306,charset="utf8")
    conn = pymysql.connect(host="rm-bp1c469j3h7ao1z07rw.mysql.rds.aliyuncs.com", user="app_readonly",password="Linzi@9527",database="risk_biz",port=3306,charset="utf8")

    # 得到一个可以执行SQL语句的光标对象
    #cursor = conn.cursor()
    # 定义要执行的SQL语句

    sql = '''
    SELECT * from arc_event  where opt_id='%s'
    '''%s1

    # 执行SQL语句
    mydf=pd.read_sql_query(sql, conn)

    # 关闭光标对象
    # cursor.close()
    # 关闭数据库连接
    conn.close()

    from  pymongo  import MongoClient

    client = MongoClient('dds-bp1f73a9a0d880741.mongodb.rds.aliyuncs.com',3717)
    # client = MongoClient('172.16.157.239',6383)
    db = client.admin    # mydb数据库，同上解释
    # db.authenticate("root", "2ICb6XyPJgdv")
    db.authenticate("root", "c4N3pVMN8zfBwhOC")
    collection = db.EVENT_INFO

    # In[12]:
    data=collection.find_one({"optId":s1})




    #必要字段检查，增加一点扩展字段

    need_lst = ['checkTime', 'checkResult','cardNo','appName','ipAddress','flowChannel','tokenId','blackBox',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion'
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
                        print('mongo:{}-> {}\t mysql: {}'.format(k,v,dfk))
            elif eval(v) in mydf.values:
                for dfk in mydf.columns:
                    if mydf[dfk].values[0]==eval(v):
                        print('mongo:{}-> {}\t mysql:{}'.format(k,v,dfk))
            else:
                print("\033[5;31;2m%s\033[0m" % k,v)
        except:
            pass
