'''
import operator
def huiwen(str1):
    str2=[]
    for each in str1:
        str2.append(each)
    str3=list(reversed(str2))
    desstr=''.join(str3)  #列表转化为字符串
    if operator.eq(str1,desstr)==True:  #operater.eq比较字符串
        print("是回文数")
    else:
        print("不是回文数")
huiwen("上海自来水来自海上")
huiwen("草草草曹")
'''

'''
def palindrome(string):
    length=len(string)
    last=length-1
    length//=2
    flag=1
    for each in range(length):
        if string[each]!=string[last]:
            flag=0
        last-=1
    if flag==1:
        return 1
    else:
        return 0
print(palindrome("上海自来水来自海上"))

'''
# def palindrome(string):
#     list1=list(string)
#     list2=list(reversed(list1))
#     if list1==list2:
#         return "是回文联"
#     else:
#         return "不是回文联"
# print(palindrome("上海自来水来自海上"))
# print(palindrome("草草曹"))
import random
result=[]
for i in range(6):
    r=random.randrange(65,99)
    result.append(chr(r))
print(''.join(result))

