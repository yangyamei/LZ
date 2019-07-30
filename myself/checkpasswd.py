# 密码安全性检查代码
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位

str=r'"~!@#$%^&*()_=-/,.?<>;:[]{}|\"' #防止被转义
num='0123456789'
zimu='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
passwd=input("请输入密码：")
length=len(passwd)
while passwd.isspace() or length==0:
    passwd=input("您的密码为空或空格请重新输入：")
#判断密码长度级别
if length<=8:
    passlenlevel=1
elif 8<length<16:
    passlenlevel=2
else:
    passlenlevel=3
#判断密码组合
passwd_flag=0
#判断是否包含特殊字符
for each in passwd:
    if each in str:
        passwd_flag+=1
        break
#判断是否包含数字
for each in passwd:
    if each in num:
        passwd_flag+=1
        break
#判断是否包含字母
for each in passwd:
    if each in zimu:
        passwd_flag+=1
        break
while 1:
    print("您的密码安全等级为:")
    if passlenlevel == 1 or passwd_flag == 1:
        print("初级")
    elif passlenlevel == 3 and passwd_flag == 3 and (passwd[0]in zimu):
        print("高级")
        break
    else:
        print("中级")
    print("请按以下方式提升您的密码安全级别：\n\
        \t1. 密码必须由数字、字母及特殊字符三种组合\n\
        \t2. 密码只能由字母开头\n\
        \t3. 密码长度不能低于16位")
    break

'''
while 1:
    if passlenlevel==1 or passwd_flag==1:
        print("您的密码等级为低级")
    elif passlenlevel==2 and passwd_flag==2:
        print("密码等级为中级")
    elif passlenlevel==3 and passwd_flag==3:
        print("密码等级为高级")
    break
'''





