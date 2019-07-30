'''
q=True
while q:
    num=input("请输入一个整数（输入Q结束程序）:")
    if num!='Q':
        num=int(num)
        print("十进制--》十六进制：%d-->0x%x"%(num,num))
        print("十进制--》八进制：%d-->0o%o"%(num,num))
        print("十进制--》二进制：%d--> "% num,bin(num))
    else:
        q=False
'''
'''
def min(x):
    least=x[0]
    for each in x:
        if each<least:
            least=each
    return least
print(min('76734567'))
'''
