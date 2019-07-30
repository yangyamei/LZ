import pymysql
import pandas as pd
from  pymongo  import MongoClient
from sqlalchemy import create_engine
#oid =input('请输入一个订单号：')
# oid = 'srxldwRJ6EF4456834107hq6'

#注释字段
sr_field_dt ={
    'logMethod':'登录方式','logTime':'登录时间 ', 'isDeviceTrust':'设备是否可信 ', 'isPhoneNumTrust':'手机号是否可信 ', 'authResult':'事件结果 ',
    'name':'姓名 ', 'idCardNo':'身份证号码 ', 'isScanIdCard':'是否有扫描身份证号码 ', 'idCardAddress':'户籍地址 ', 'idCardNation':'民族 ',
    'idCardCreateTime':'身份证有效期开始时间 ', 'idCardEndTime':'身份证有效期结束时间 ', 'idCardBirtherDay':'生日 ', 'idCardIssuanceAuthority':'签发机关 ', 'idCardFrontPhoto':'身份证正面照片 ', 'idCardOppositePhoto':'身份证反面照片 ', 'eventBeginTime':'事件开始时间 ', 'eventEndTime':'事件结束时间 '
    , 'faceReplaced':'是否检测出换脸 ', 'authResult':'调用face++是否成功 ', 'confidence':'相似度 ', 'liveness':'活体认证返回结果 ', 'syntheticFaceConfidence':'人脸照片为软件合成脸的置信度 ', 'maskConfidence':'人脸照片为面具的置信度 ', 'screenReplayConfidence':'人脸照片为屏幕翻拍的置信度 ',
    'realName':'用户真实姓名 ', 'idCardNo':'用户真实身份证号码 ', 'phoneNum':'手机号码 ', 'validateChannel':'验证数据正确性方式 ',

    'phoneInputContent':'输入手机号内容','inputBankCard':'输入卡号 ', 'accountBank':'开户行 ', 'codeValidResult':'短信验证结果 ', 'authResult':'事件结果 ',
    'codeValidResult':'短信验证结果 ',
    'codeValidType':'验证码类型 ', 'codeSendTime':'验证码发送时间 ', 'isSend':'是否发送成功 ',''
    'borrowNo':'订单号 ','amount':'订单金额 ', 'maxOverdueDays':'最大逾期天数 ', 'installmentCnt':'账单总期数 ',  'billMaxOverdueDay':'当次账单最大逾期天数 ', 'billMinOverdueDay':'当次账单最小逾期天数 ', 'billNo':'当次账单期数 ', 'billIncome':'当次账单收益 '
    , 'isSettle':'是否本笔结清 ', 'income':'订单收益 ', 'overdueDays':'逾期天数 ', 'overdueCount':'逾期次数 ', 'time':'借款时间 ', 'poundage':'手续费 ', 'realAmount':'实际交易金额，分期总金额 ', 'orderAmount':'订单金额 ', 'nper':'分期期数 '
    , 'inLoanOverdueDay':'在借订单中未还账单逾期最大天数 ', 'isCycleBorrow':'是否循环借款 ', 'orderNo':'订单号 ',


    'borrowStatus':'借款状态 ', 'relation':'社会关系 ','houseAddress':'家庭住址','company':'公司名称', 'workAddress':'公司地址',

    'borrowAmount':'订单金额（借款金额）','borrowType':'借款类型 ', 'productType':'产品类型 ', 'billNo':'(子)账单ID） ','amount':'(子)账单金额 ', 'installmentCnt':'分期总期数 ', 'interest':'本期利息（利息） ', 'installmentNo':'第几期还款 ', 'overdueAmount':'本期逾期利息（逾期费用） ', 'repaymentNo':'还款编号 ',
    'repaymentType':'还款类型 ', 'isPartPay':'是否部分还款 ', 'isAllPayOff':'该用户是否已还清全部借款 ', 'isPayOff':'当前分期是否还清 ', 'repaymentState':'还款情况 ', 'guaranteesCash':'担保费 ', 'overdueDay':'逾期天数 ', 'repaymentStatus':'还款状态 '
    , 'repaymentAmount':'实际还款金额 ', 'actualPaymentAmount':'实际支付金额 ', 'repaymentFailReason':'还款失败原因 ', 'discountId':'用户使用的还款券 ', 'discountName':'优惠名称 ', 'availableAmount':'可用额度 ', 'discountPrice':'优惠价格 ', 'usedAmount':'已用额度 ', 'creditAmount':'授信额度 '
    , 'preIncome':'前置利息 ', 'borrowCash':'实际交易金额 ', 'borrowTime':'借款时间 ','payCashTime':'打款时间','maxRepaymentTime':'计划还款时间 ', 'installmentCnt':'分期总期数 ',

    'name':'联系人姓名 ', 'idNo':'身份证 ', 'devType':'设备类型 ', 'ipAddress':'IP地址 ', 'flowChannel':'流量渠道（my钱包用） ', 'appName':'同盾应用名称 ', 'checkTime':'风控审核时间 ',
    'phone':'注册手机号 ',

    'borrow':'中文123','checkResult':'风控审核结果 ', 'tokenId':'设备指纹（网页版） ', 'blackBox':'设备指纹（移动端原生SDK接入） ', 'cardNo':'银行卡号 ', 'devType':'设备类型 ', 'ipAddress':'IP地址 ', 'flowChannel':'流量渠道（my钱包用） ','quotaChannelType':'渠道建议额度区间', 'appName':'同盾应用名称 ', 'checkTime':'风控审核时间 ',
    'phone':'注册手机号 ', 'ipAddr':'ip地址 ', 'coordinateX':'经度 ', 'coordinateY':'纬度（注意不要传反了） ', 'devType':'设备类型 ', 'devOs':'操作系统 ', 'devOsVersion':'操作系统版本 ', 'appVersion':'app版本 '
    , 'devId':'设备号 ', 'serialNum':'硬件序列号 ', 'wifiName':'wifi名称 ', 'bssid':'bssid ', 'electricity':'手机电量 ', 'storage':'手机存储量 ', 'storageUsed':'手机已用存储量 ', 'isCharging':'是否正在充电 ', 'gyroscopeX':'陀螺仪X '
    , 'gyroscopeY':'陀螺仪Y ', 'gyroscopeZ':'陀螺仪Z ', 'isRoot':'是否越狱或者root ',

    'fundsProvider':'资金方 ',
    'education':'学历 ','marriage':'婚姻状况 ','workingYears':'工作年限 ','workAddressDetail':'单位详细地址 '

    }
#强风控
sr_need_lst = ['checkResult', 'tokenId', 'blackBox', 'cardNo', 'devType', 'ipAddress', 'flowChannel','quotaChannelType', 'appName', 'checkTime',
               'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion', 'devId', 'serialNum', 'wifiName', 'bssid'
    , 'electricity', 'storage', 'storageUsed', 'isCharging', 'gyroscopeX', 'gyroscopeY', 'gyroscopeZ', 'isRoot']
#弱风控
wr_need_lst = ['fundsProvider','checkTime', 'checkResult', 'time', 'poundage', 'realAmount', 'orderAmount', 'nper', 'orderNo','inLoanOverdueDay','isCycleBorrow'
    ,'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion', 'devId', 'serialNum', 'wifiName', 'bssid'
    , 'electricity', 'storage', 'storageUsed', 'isCharging', 'gyroscopeX', 'gyroscopeY', 'gyroscopeZ', 'isRoot']
#实名
sm_need_lst = ['realName', 'idCardNo', 'phoneNum', 'eventBeginTime', 'validateChannel', 'eventEndTime',
               'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion', 'devId', 'serialNum', 'wifiName', 'bssid'
    , 'electricity', 'storage', 'storageUsed', 'isCharging', 'gyroscopeX', 'gyroscopeY', 'gyroscopeZ', 'isRoot']
#扫脸
sl_need_lst = [ 'eventBeginTime', 'eventEndTime', 'faceReplaced', 'authResult', 'confidence', 'liveness', 'syntheticFaceConfidence', 'maskConfidence', 'screenReplayConfidence',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion', 'devId', 'serialNum', 'wifiName', 'bssid'
    , 'electricity', 'storage', 'storageUsed', 'isCharging', 'gyroscopeX', 'gyroscopeY', 'gyroscopeZ', 'isRoot']
#身份
sf_need_lst = ['name', 'idCardNo', 'isScanIdCard', 'idCardAddress', 'idCardNation', 'idCardCreateTime', 'idCardEndTime', 'idCardBirtherDay', 'idCardIssuanceAuthority', 'idCardFrontPhoto', 'idCardOppositePhoto', 'eventBeginTime', 'eventEndTime',
               'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion', 'devId', 'serialNum', 'wifiName', 'bssid'
    , 'electricity', 'storage', 'storageUsed', 'isCharging', 'gyroscopeX', 'gyroscopeY', 'gyroscopeZ', 'isRoot']
#通讯录
tx_need_lst = ['eventBeginTime', 'eventEndTime', 'codeValidResult', 'authResult',
               'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion', 'devId', 'serialNum', 'wifiName', 'bssid'
    , 'electricity', 'storage', 'storageUsed', 'isCharging', 'gyroscopeX', 'gyroscopeY', 'gyroscopeZ', 'isRoot']
#绑卡
bk_need_lst = ['eventBeginTime', 'eventEndTime', 'phoneInputContent', 'inputBankCard', 'accountBank', 'codeValidResult', 'authResult',
               'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion', 'devId', 'serialNum', 'wifiName', 'bssid'
    , 'electricity', 'storage', 'storageUsed', 'isCharging', 'gyroscopeX', 'gyroscopeY', 'gyroscopeZ', 'isRoot']
#短信
dx_need_lst = ['codeValidType', 'codeSendTime', 'isSend',
               'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion', 'devId', 'serialNum', 'wifiName', 'bssid'
    , 'electricity', 'storage', 'storageUsed', 'isCharging', 'gyroscopeX', 'gyroscopeY', 'gyroscopeZ', 'isRoot']
#提降额
te_need_lst = ['borrowNo', 'amount', 'maxOverdueDays', 'installmentCnt',  'billMaxOverdueDay', 'billMinOverdueDay', 'billNo', 'billIncome', 'isSettle', 'income', 'overdueDays', 'overdueCount',
               'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion', 'devId', 'serialNum', 'wifiName', 'bssid'
    , 'electricity', 'storage', 'storageUsed', 'isCharging', 'gyroscopeX', 'gyroscopeY', 'gyroscopeZ', 'isRoot']
#借款
bs_need_lst = ['borrowNo', 'usedAmount', 'availableAmount', 'creditAmount', 'preIncome', 'borrowCash', 'borrowTime', 'payCashTime', 'maxRepaymentTime', 'installmentCnt', 'borrowStatus',
               'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion', 'devId', 'serialNum', 'wifiName', 'bssid'
    , 'electricity', 'storage', 'storageUsed', 'isCharging', 'gyroscopeX', 'gyroscopeY', 'gyroscopeZ', 'isRoot']
#还款
re_need_lst = ['borrowNo', 'borrowAmount', 'borrowType', 'productType', 'billNo', 'amount', 'installmentCnt', 'interest', 'installmentNo', 'overdueAmount', 'income', 'repaymentNo', 'repaymentType', 'isPartPay', 'isAllPayOff', 'isPayOff', 'repaymentState', 'guaranteesCash', 'overdueDay', 'repaymentStatus', 'repaymentAmount', 'actualPaymentAmount', 'repaymentFailReason', 'discountId', 'discountName', 'availableAmount', 'discountPrice',
               'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion', 'devId', 'serialNum', 'wifiName', 'bssid'
    , 'electricity', 'storage', 'storageUsed', 'isCharging', 'gyroscopeX', 'gyroscopeY', 'gyroscopeZ', 'isRoot']
#紧急联系人
al_need_lst = [ 'eventBeginTime', 'eventEndTime','relation', 'name', 'idNo', 'phone', 'houseAddress', 'company', 'workAddress',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion', 'devId', 'serialNum', 'wifiName', 'bssid'
    , 'electricity', 'storage', 'storageUsed', 'isCharging', 'gyroscopeX', 'gyroscopeY', 'gyroscopeZ', 'isRoot']
#预授信
pc_need_lst = [ 'checkResult', 'checkTime', 'cardNo', 'appName', 'ipAddress', 'blackBox', 'flowChannel', 'tokenId',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion', 'devId', 'serialNum', 'wifiName', 'bssid'
    , 'electricity', 'storage', 'storageUsed', 'isCharging', 'gyroscopeX', 'gyroscopeY', 'gyroscopeZ', 'isRoot']
#额度激活
qa_need_lst = [  'checkResult', 'eventBeginTime', 'checkTime', 'fundsProvider',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion', 'devId', 'serialNum', 'wifiName', 'bssid'
    , 'electricity', 'storage', 'storageUsed', 'isCharging', 'gyroscopeX', 'gyroscopeY', 'gyroscopeZ', 'isRoot']
#额度失效
is_need_lst = [ 'checkResult', 'eventBeginTime', 'checkTime', 'fundsProvider',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion', 'devId', 'serialNum', 'wifiName', 'bssid'
    , 'electricity', 'storage', 'storageUsed', 'isCharging', 'gyroscopeX', 'gyroscopeY', 'gyroscopeZ', 'isRoot']
#预风控
pr_need_lst = [ 'checkTime', 'tokenId', 'blackBox', 'cardNo', 'devType', 'ipAddress', 'appName', 'checkResult',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion', 'devId', 'serialNum', 'wifiName', 'bssid'
    , 'electricity', 'storage', 'storageUsed', 'isCharging', 'gyroscopeX', 'gyroscopeY', 'gyroscopeZ', 'isRoot']
#补充资料认证事件
ad_need_lst = ['eventBeginTime', 'eventEndTime', 'education', 'marriage', 'company', 'workingYears', 'workAddress', 'workAddressDetail',
                'phone', 'ipAddr', 'coordinateX', 'coordinateY', 'devType', 'devOs', 'devOsVersion', 'appVersion', 'devId', 'serialNum', 'wifiName', 'bssid'
    , 'electricity', 'storage', 'storageUsed', 'isCharging', 'gyroscopeX', 'gyroscopeY', 'gyroscopeZ', 'isRoot']
dt = {'sr':'||||强风控事件||||','sm':'||||实名认证事件||||','sl':'||||扫脸认证事件||||','sf':'||||身份认证事件||||','tx':'||||通讯录认证事件||||','bk':'||||绑卡事件||||','dx':'||||短信认证事件||||',
      'te':'||||提降额事件||||(缺少当次账单逾期天数)','wr':'||||弱风控事件||||','bs':'||||借款事件||||','re':'||||还款事件||||','al':'||||紧急联系人事件||||','pc':'||||预授信事件||||','qa':'||||额度激活事件||||','is':'||||额度失效事件||||',
      'pr':'||||预风控事件||||','ad':'||||补充资料认证事件||||',}

def get_mysql(oid):
    host = '101.37.106.150'
    engine = create_engine('mysql+pymysql://riskc_user:Lz@091988@{}:3306/arc_lz'.format(host))

    sql = '''
    SELECT * from arc_event  where opt_id='%s'
    '''% oid
    df = pd.read_sql(sql,engine)
    return df

def get_mongo(oid):
    client = MongoClient(host='172.16.157.239',port=6383)

    db = client['admin']
    db.authenticate("root", "2ICb6XyPJgdv")
    collection = db['EVENT_INFO']
    return collection.find_one({"optId":'%s'%oid})

def test_result(oid):
    need_lst = eval(oid[:2]+'_need_lst')
    field_dt = eval('sr'+'_field_dt')
    jieguo_list=[]
    jieguo_list.append(dt[oid[:2]])
    mydf = get_mysql(oid)
    data = get_mongo(oid)
    if data is None:
        return "订单号不存在或查询为空，请检查后重新输入"

    for nl in need_lst:
        if nl not in data.keys():
            jieguo_list.append('{}{}              ->               无该字段'.format(field_dt[nl],nl))
        else:
            jieguo_list.append('"{}{:20}"->"{:>50}"'.format(field_dt[nl],nl,data[nl]))

    for k,v in data.items():
        try:
            if v in mydf.values:
                for dfk in mydf.columns:
                    if mydf[dfk].values[0]==v:
                        jieguo_list.append('mongo:{}-> {}{}mysql: {}'.format(k,v,dfk))
            elif eval(v) in mydf.values:
                for dfk in mydf.columns:
                    if mydf[dfk].values[0]==eval(v):
                        jieguo_list.append('mongo:{}-> {}{}mysql:{}'.format(k,v,dfk))
            else:
                jieguo_list.append("\033[5;31;2m%s\033[0m" % k,v)
        except:
            pass
    return jieguo_list
# test_result(oid)

