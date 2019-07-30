def compare_file(file1,file2):
    f1=open(file1,encoding='utf-8')
    f2=open(file2,encoding='utf-8')
    count=0 #统计行数
    differ=[] #统计不一样的数量
    for line1 in f1:
        line2=f2.readline()
        count+=1
        if line1!=line2:
            differ.append(count)
    f1.close()
    f2.close()
    return differ
file1=input("请输入第一个文件名：")
file2=input("请输入第2个文件名：")
differ=compare_file(file1,file2)
if len(differ)==0:
    print("2个文件完全一样")
else:
    print("2个文件共有%d处不同"% len(differ))
    for each in differ:
        print("第%d行不一致"% each)


