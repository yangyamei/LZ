#

from sjhs import Acard   #强风控
from sjhs import Bcard   #弱风控，借款审核事件
from sjhs import Borrowingevent
from sjhs import Carriercertificationevent
from sjhs import Faceverificationevent
from sjhs import Liftingamount
from sjhs import Offlinerepayment
from sjhs import Realnamecertificationevent   #实名认证
from sjhs import Registrationoperation
from sjhs import Repaymentevent #还款事件
from sjhs import Advancecredit  #预风控同预授信
from sjhs import Loginsynchronizationevent
from sjhs import Logintoanasynchronousevent
from sjhs import SMSevent
from sjhs import tiedcardcertification  #绑卡认证
from sjhs import identityauthentication  #身份认证
from sjhs import Modifytheloginpassword #修改登录密码
from sjhs import PhoneBook  #通讯录
from sjhs import PreControl  #预风控
from sjhs import EmergencyContact #紧急联系人
from sjhs import pre_approval   #预授信
from sjhs import zhuce
from sjhs import ModifythePayinpassword  #修改支付密码
from sjhs import Findloginpassword  #找回登录密码
#Faceverificationevent 扫脸认证
#Carriercertificationevent 运营商认证
#-----Borrowingevent 借款事件
#Offlinerepayment线下还款
#Liftingamount  提降额
#短信事件SMSevent
#登录异步Logintoanasynchronousevent
#注册事件Registrationoperation
#Advancecredi预授信
#登录同步Loginsynchronizationevent
#输入时间类型
type=Liftingamount
#输入订单号
optid='teqbblRJ78J142877210000c'
# borrowNo='jkbUJ4HJ5843236100005'
#srqbblRJ3VG104436210002w
#srqbblRJ3VG1027426100015
if type==Acard:
    print(type(optid))
elif type==Bcard:
    print(type(optid))
elif type==Borrowingevent:
    print(type(optid))
elif type==Carriercertificationevent:
    print(type(optid))
elif type==Faceverificationevent:
    print(type(optid))
elif type==Liftingamount:
    print(type(optid))
elif type==Offlinerepayment:
    print(type(optid))
elif type==Realnamecertificationevent:
    print(type(optid))
elif type==Registrationoperation:
    print(type(optid))
elif type==Repaymentevent:
    print(type(optid))
elif type==Advancecredit:
    print(type(optid))
elif type==Loginsynchronizationevent:
    print(type(optid))
elif type==Logintoanasynchronousevent:
    print(type(optid))
elif type==SMSevent:
    print(type(optid))
elif type == tiedcardcertification:
    print(type(optid))
elif type == identityauthentication:
    print(type(optid))
elif type == Modifytheloginpassword:
    print(type(optid))
elif type == PhoneBook:
    print(type(optid))
elif type == PreControl:
    print(type(optid))
elif type == EmergencyContact:
    print(type(optid))
elif type==pre_approval:
    print(type(optid))
elif type==zhuce:
    print(type(optid))
elif type==ModifythePayinpassword:
    print(type(optid))
elif type==Findloginpassword:
    print(type(optid))