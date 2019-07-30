
import os
import os.path
def filesize(path):
    os.chdir(path)
    for file in os.listdir(path):
        #file=os.path.join(path,file)  #将listdir()返回的数据拼接成绝对路径传入os.path.isfile()
        if os.path.isfile(file)==True:
            print("文件%s的大小为【%s】"%(file,os.path.getsize(file)))
        else:
            print("%s不是文件"% file)
path=input("请输入路径：")
filesize(path)







