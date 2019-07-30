user = {}
# def menu():
#     prompt='''
# |-------新建用户：N/n------|
# |-------登录账号：E/e------|
# |-------退出程序：Q/q------|
# |-------请输入指令代码：'''
#     while True:
#         chosen=False
#         while not chosen:
#             command=input(prompt)
#             if command not in 'NnEeQq':
#                 print("指令代码错误，请重新输入：")
#             else:
#                 chosen=True
#         if command=="N" or command=="n":
#             adduser()
#         elif command=="E" or command=="e":
#             login()
#         elif command=="Q" or command=="q":
#             break
def menu():
    print("|-------新建用户：N/n------|")
    print("|-------登录账号：E/e------|")
    print("|-------退出程序：Q/q------|")
    while 1:
        command=input("请输入指令代码：")
        if command == "N" or command == "n":
            adduser()
        elif command=="E" or command=="e":
            login()
        elif command=="Q" or command=="q":
            break
#新建用户
def adduser():
    username=input("请输入用户名：")
    passwd=input("请输入密码：")
    if username in user:
        print(input("此用户名已存在，请重新输入"))
    else:
        user.setdefault(username,passwd)
        print("注册成功，赶紧试试登录吧")
def login():
    username=input("请输入用户名")
    if username not in user:
        print(input("用户名不存在，请重新输入："))
        passwd=input("请输入密码：")
        print("欢迎进入xx系统~~~")
    else:
        passwd = input("请输入密码：")
        print("欢迎进入xx系统")
menu()

