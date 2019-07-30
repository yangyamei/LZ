'''
插入联系人

print('|---欢迎进入通讯录程序---|')
print('|---1.查询联系人资料---|')
print('|---2.插入新的联系人---|')
print('|---3.删除已有联系人---|')
print('|---4.退出通讯录程序---|')
contacts={}
while 1:
    selectnum=(int)(input("请输入相关的指令代码："))
    if selectnum==1:
        for k,v in contacts.items():
            print(k+':'+v)
    elif selectnum==2:
        name=input("请输入姓名：")
        phone=input("请输入号码：")
        # for k,v in contacts.items():
        #     if phone==v and name==k:
        #         print("号码已存在")
        #     else:
        contacts.setdefault(name,phone)
    elif selectnum==3:
        name=input("请输入需要删除号码姓名")
        for k, v in contacts.items():
            if name==k:
                contacts.pop(k)
            else:
                print("姓名不存在，请继续")
                continue
    elif selectnum==4:
        break
'''
print('|---欢迎进入通讯录程序---|')
print('|---1.查询联系人资料---|')
print('|---2.插入新的联系人---|')
print('|---3.删除已有联系人---|')
print('|---4.退出通讯录程序---|')
contacts=dict()
while 1:
    instr=int(input("\n请输入相关的指令代码："))
    if instr==1:
        name=input("请输入联系人姓名：")
        if name in contacts:
            print(name+":"+contacts[name])
        else:
            print("您输入的姓名不在通讯录中")
    if instr==2:
        name=input("请输入联系人姓名：")
        if name in contacts:
            print("您输入的姓名在通讯录中已存在--》",end=' ')
            print(name + ":" + contacts[name])
            if input("是否修改用户资料（Yes/No)"=='Yes'):
                contacts[name]=input("请输入电话号码：")
    else:
        contacts[name]=input("请输入用户联系电话：")
    if instr==3:
        name=input("请输入要删除的用户姓名：")
        if name in contacts:
            del(contacts[name])
        else:
            print("您输入的用户不存在")
    if instr==4:
        break
print("|-------感谢使用通讯录程序-------|")





